from .html import Tag


class _Header(Tag):
    _possible_attrs = {'align'}


class H1(_Header):
    ...


class H2(_Header):
    ...


class H3(_Header):
    ...


class H4(_Header):
    ...


class H5(_Header):
    ...


class H6(_Header):
    ...
