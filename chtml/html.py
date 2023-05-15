import copy
from contextlib import contextmanager
from datetime import date, datetime
from decimal import Decimal
from typing import Iterable, List, Mapping, Optional, Union

_TEXT = Optional[Union[str, int, date, datetime, Decimal]]
_STYLE = Optional[Mapping[str, str]]
_CHILDREN = Optional[List['Tag']]
_PROPERTIES = Optional[Mapping[str, str]]

_single_tags = (
    'br', 'meta', 'link', 'hr', 'img', 'input', 'base', 'area',
    'col', 'embed', 'param', 'source', 'wbr', 'track', 'keygen',
)


class Tag:

    _possible_attrs = set()

    _global_attrs = {
        'id', 'class', 'style', 'lang', 'tabindex', 'title', 'spellcheck'
    }

    def __init__(
            self,
            text: _TEXT = None,
            style: _STYLE = None,
            children: _CHILDREN = None,
            attrs: _PROPERTIES = None,
            id_: Optional[str] = None,
            class_: Optional[str] = None,
    ):
        self._tag = self.__class__.__name__.lower()

        if attrs:
            possible_attrs = self._possible_attrs.union(self._global_attrs)
            for attr in attrs:
                if attr not in possible_attrs:
                    raise ValueError(f'Attribute "{attr}" not allowed for tag <{self._tag}>')

        if text and self._tag in _single_tags:
            raise ValueError('Text cannot be specified for single tag')

        self._text = str(text) if text else ''
        self._children = children or []
        self._attrs = attrs or {}

        if id_:
            self._attrs.update({'id': id_})
        if class_:
            self._attrs.update({'class': class_})

        if style:
            if not isinstance(style, Mapping):
                raise TypeError('Expect `Mapping` type, but actual "%s"' % type(style))
            self._style = copy.deepcopy(style)
        else:
            self._style = {}

    def add_child(self, tag: 'Tag'):
        if not isinstance(tag, Tag):
            raise TypeError('Expect `Tag` type, but actual "%s"' % type(tag))
        if self._tag in _single_tags:
            raise ValueError('Child tag cannot be added for single tag')
        self._children.append(tag)

    def update_style(self, **styles):
        self._style.update(styles)

    def update_attrs(self, **attrs):
        possible_attrs = self._possible_attrs.union(self._global_attrs)
        for attr in attrs:
            if attr not in possible_attrs:
                raise ValueError(f'Attribute "{attr}" not allowed for tag <{self._tag}>')
        self._attrs.update(attrs)

    def update_text(self, text: str):
        if not isinstance(text, str):
            raise TypeError('Invalid type of text')
        self._text = text

    def _get_css(self) -> str:
        if not self._style:
            return ''
        styles = []
        for style, value in self._style.items():
            styles.append(f'{style}:{value}')
        return f'style="{";".join(styles)}"'

    def _get_attrs(self) -> str:
        if not self._attrs:
            return ''
        attrs = []
        for attr, value in self._attrs.items():
            attrs.append(f'{attr}="{value}"')
        return ' '.join(attrs)

    def _open_tag(self) -> str:
        tag = []
        for part in (self._tag, self._get_css(), self._get_attrs()):
            if part:
                tag.append(part)
        return f'<{" ".join(tag)}>'

    def _close_tag(self) -> str:
        if self._tag in _single_tags:
            raise ValueError('Close tag does not exist for single tag')
        return f'</{self._tag}>'

    def to_html(self) -> str:
        if not self._children:
            if self._tag in _single_tags:
                return self._open_tag()
            return ''.join([
                self._open_tag(),
                self._text,
                self._close_tag(),
            ])
        result = self._open_tag() + self._text
        for child in self._children:
            result += child.to_html()
        return result + self._close_tag()


class Html(Tag):

    _possible_attrs = {'manifest'}

    def __init__(self, attrs: _PROPERTIES = None, children: _CHILDREN = None):
        super().__init__(
            attrs=attrs,
            children=children,
        )
        self._body: Optional['Body'] = None
        self._head: Optional['Head'] = None

    @property
    def head(self) -> 'Head':
        if self._head is None:
            for child in self._children:
                if isinstance(child, Head):
                    self._head = child
                    break
            else:
                raise TypeError('Head is None')
        return self._head

    @property
    def body(self) -> 'Body':
        if self._body is None:
            for child in self._children:
                if isinstance(child, Body):
                    self._body = child
                    break
            else:
                raise TypeError('Body is None')
        return self._body

    def save(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.to_html())


class Head(Tag):

    def __init__(self, children: _CHILDREN = None):
        super().__init__(children=children)


class Link(Tag):

    _possible_attrs = {'charset', 'href', 'rel', 'type', 'media'}

    def __init__(self, attrs: _PROPERTIES = None,):
        super().__init__(attrs=attrs)


class Style(Tag):

    _possible_attrs = {'media', 'type'}

    def __init__(self, styles: str, attrs: _PROPERTIES = None):
        super().__init__(text=styles, attrs=attrs)


class Meta(Tag):

    _possible_attrs = {'charset', 'content', 'http-equiv', 'name'}

    def __init__(self, attrs: _PROPERTIES = None,):
        super().__init__(attrs=attrs)


class Body(Tag):

    def __init__(self, style: _STYLE = None, children: _CHILDREN = None):
        super().__init__(style=style, children=children)


@contextmanager
def get_html(filename: str, style: Optional[Style] = None, links: Optional[Iterable[Link]] = None) -> Html:
    body = Body()
    meta = Meta(attrs={'charset': 'utf-8'})
    hchildren = [meta]
    if style is not None:
        if not isinstance(style, Style):
            raise TypeError(f'Expect `Style` type, but actual {type(style)}')
        hchildren.append(style)
    if links is not None:
        for link in links:
            if not isinstance(link, Link):
                raise TypeError(f'Expect `Link` type, but actual {type(style)}')
            hchildren.append(link)
    head = Head(children=hchildren)
    html = Html(children=[head, body])
    try:
        yield html
    finally:
        with open(filename, 'w') as file:
            file.write(html.to_html())
