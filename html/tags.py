from html.html import Tag


class Br(Tag):
    _global_attrs = set()
    _possible_attrs = set()

    def __init__(self):
        super().__init__()


class A(Tag):
    _possible_attrs = {'href', 'name', 'type', 'target', 'rel'}


class Hr(Tag):
    _global_attrs = {'id', 'class', 'style'}


class Div(Tag):
    ...


class Span(Tag):
    ...
