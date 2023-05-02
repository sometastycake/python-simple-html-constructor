from html.html import Tag


class Table(Tag):
    _possible_attrs = {
        'align', 'border', 'bgcolor', 'width',
        'summary', 'cellspacing', 'cellpadding',
    }


class Caption(Tag):
    _possible_attrs = {'align'}


class THead(Tag):
    _possible_attrs = {'align'}


class TBody(Tag):
    _possible_attrs = {'align'}


class TFoot(Tag):
    _possible_attrs = {'align'}


class ColGroup(Tag):
    _possible_attrs = {'span'}


class Col(Tag):
    _possible_attrs = {'span'}


class Tr(Tag):
    ...


class Td(Tag):
    _possible_attrs = {
        'colspan', 'rowspan',
        'scope', 'align', 'valign',
    }


class Th(Td):
    _possible_attrs = Td._possible_attrs
    _possible_attrs.update({'align'})
