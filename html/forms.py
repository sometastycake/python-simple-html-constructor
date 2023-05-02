from .html import Tag


class Form(Tag):
    _possible_attrs = {
        'name', 'action', 'enctype',
        'method', 'accept-charset',
    }


class Input(Tag):
    _possible_attrs = {
        'align', 'alt', 'form', 'formaction', 'formenctype',
        'formmethod', 'formtarget', 'list', 'max', 'maxlength',
        'min', 'name', 'pattern', 'placeholder', 'size', 'src',
        'step', 'type', 'value', 'accesskey',
    }


class TextArea(Tag):
    _possible_attrs = {
        'cols', 'form', 'maxlength', 'name',
        'placeholder', 'rows', 'wrap', 'accesskey',
    }


class Label(Tag):
    _possible_attrs = {'accesskey', 'for'}


class FieldSet(Tag):
    _possible_attrs = {'form', 'title'}


class Legend(Tag):
    _possible_attrs = {'accesskey', 'align', 'title'}


class Select(Tag):
    _possible_attrs = {'accesskey', 'form', 'name', 'size'}


class OptGroup(Tag):
    _possible_attrs = {'label'}


class Option(Tag):
    _possible_attrs = {'label', 'value'}


class Button(Tag):
    _possible_attrs = {
        'accesskey', 'form', 'formaction', 'formenctype',
        'formmethod', 'formtarget', 'name', 'type', 'value',
    }
