from html.html import Tag


class Ul(Tag):
    _possible_attrs = {'type'}


class Ol(Tag):
    _possible_attrs = {'type', 'start'}


class Li(Tag):
    _possible_attrs = {'type', 'value'}


class Dl(Tag):
    ...


class Dd(Tag):
    ...


class Dt(Tag):
    ...
