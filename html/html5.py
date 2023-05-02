from .html import Tag


class Article(Tag):
    ...


class Aside(Tag):
    ...


class Audio(Tag):
    _possible_attrs = {'controls', 'loop', 'preload', 'src'}


class Canvas(Tag):
    _possible_attrs = {'height', 'width'}


class DataList(Tag):
    ...


class Details(Tag):
    _possible_attrs = {'open'}


class FigCaption(Tag):
    ...


class Figure(Tag):
    ...


class Footer(Tag):
    ...


class Header(Tag):
    ...


class Main(Tag):
    ...


class Nav(Tag):
    ...


class Progress(Tag):
    _possible_attrs = {'value', 'max'}


class Section(Tag):
    ...


class Summary(Tag):
    ...


class Time(Tag):
    _possible_attrs = {'datetime'}


class Video(Tag):
    _possible_attrs = {
        'height', 'video', 'src', 'controls', 'poster',
    }
