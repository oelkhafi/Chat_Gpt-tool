from functools import total_ordering


@total_ordering
class Book:
    """"""класс книга""""""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __getitem__(self, key):
        if key < 1 or key > len(self._content):
            raise PageNotFoundError
        return self._content[key - 1]

    def __setitem__(self, key, value):
        if key < 1 or key > len(self._content):
            raise PageNotFoundError
        self._content[key - 1] = Page(str(value))

    def __len__(self):
        return len(self._content)

    def __eq__(self, other):
        if isinstance(other, Book):
            return len(self) == len(other)
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Book):
            return len(self) < len(other)
        raise TypeError


@total_ordering
class Page:
    """"""класс страница""""""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    def __str__(self):
        return self._text

    def __repr__(self):
        return self._text

    def __add__(self, other):
        if not isinstance(other, (Page, str)):
            raise TypeError
        other = str(other)
        if len(self) + len(other) > self.max_sign:
            raise TooLongTextError
        self._text += other
        return self

    def __radd__(self, other):
        if not isinstance(other, (Page, str)):
            raise TypeError
        return str(other) + str(self)

    def __iadd__(self, other):
        if not isinstance(other, (Page, str)):
            raise TypeError
        other = str(other)
        if len(self) + len(other) > self.max_sign:
            raise TooLongTextError
        self._text += other
        return self

    def __len__(self):
        return len(self._text)

    def __eq__(self, other):
        if isinstance(other, (Page, str)):
            return len(self) == len(other)
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, (Page, str)):
            return len(self) < len(other)
        raise TypeError 