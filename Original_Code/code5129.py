class Person:
    """"""класс описывающий человека""""""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def read(book, page):
        """"""читаем страницу page в книге book""""""
        return book.read(page)

    @staticmethod
    def write(book, page, text):
        """"""пишем на страницу page в книге book""""""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """"""устанавливает закладку в книгу book""""""
        if hasattr(book, 'set_bookmark'):
            book.set_bookmark(self, page)
            return
        raise NotExistingExtensionError

    def get_bookmark(self, book):
        """"""получает номер страницы установленной закладки в книге book""""""
        if hasattr(book, 'get_bookmark'):
            return book.get_bookmark(self)
        raise NotExistingExtensionError

    def del_bookmark(self, book):
        """"""удаляет закладку читателя person, если она установлена""""""
        if hasattr(book, 'get_bookmark'):
            book.del_bookmark(self)
            return
        raise NotExistingExtensionError


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, *args, **kwargs):
        raise NotImplementedError

    def write(self, *args, **kwargs):
        raise NotImplementedError


class Novel(Book):
    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author  # автор
        self.year = year  # год издания
        self.bookmark = {}  # словарь: ключ-читатель,значение-номер страницы

    def read(self, page):
        """"""возвращает страницу""""""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, *args, **kwargs):
        raise PermissionDeniedError

    def set_bookmark(self, person, page):
        """"""устанавливает закладку в книгу book""""""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """"""получает номер страницы установленной закладки в книге book""""""
        if person in self.bookmark:
            return self.bookmark[person]
        raise PageNotFoundError

    def del_bookmark(self, person):
        if person in self.bookmark:
            del self.bookmark[person]


class Notebook(Book):
    def __init__(self, title, size=12, max_sign=2000, content=None):
        content = content if content else ['', ] * size
        super().__init__(title, content)
        self.max_sign = max_sign  # максимальное количество символов на странице

    def read(self, page):
        """"""возвращает страницу""""""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, page, text):
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        if len(self.content[page]) + len(text) > self.max_sign:
            raise TooLongTextError
        self.content[page] += text
  
 