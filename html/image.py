from html.html import Tag


class Img(Tag):
    _possible_attrs = {
        'width', 'height', 'align', 'alt',
        'src', 'usemap', 'ismap',
    }
