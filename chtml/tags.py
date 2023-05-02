from typing import Optional

from .html import Tag, _PROPERTIES


class Br(Tag):
    _global_attrs = set()
    _possible_attrs = set()

    def __init__(self):
        super().__init__()


class A(Tag):
    _possible_attrs = {'href', 'name', 'type', 'target', 'rel'}


class Hr(Tag):
    _global_attrs = {'id', 'class', 'style'}

    def __init__(
        self, styles: str,
        attrs: _PROPERTIES = None,
        id_: Optional[str] = None,
        class_: Optional[str] = None
    ):
        super().__init__(text=styles, attrs=attrs, id_=id_, class_=class_)


class Div(Tag):
    ...


class Span(Tag):
    ...
