class Person:
    """"""класс описывающий человека""""""

    def __init__(self, name):
        self.name = name

    def set_bookmark(self, *args, **kwargs):
        """"""устанавливает закладку в книгу book""""""
        raise NotImplementedError

    def get_bookmark(self, *args, **kwargs):
        """"""получает номер страницы установленной закладки в книге book""""""
        raise NotImplementedError

    def del_bookmark(self, *args, **kwargs):
        """"""удаляет закладку читателя person, если она установлена""""""
        raise NotImplementedError


class Reader:
    def read(self, book, num_page):
        return book[num_page]


class Writer:
    def write(self, book, num_page, text):
        book[num_page] += text


class AdvancedPerson(Person, Reader, Writer):
    """"""класс человека умеющего читать, писать, пользоваться закладками""""""

    @staticmethod
    def set_bookmark(book, num_page):
        """"""устанавливает закладку в книгу book""""""
        if not hasattr(book, 'bookmark'):
            raise NotExistingExtensionError
        book.bookmark = num_page

    @staticmethod
    def get_bookmark(book):
        """"""получает номер страницы установленной закладки в книге book""""""
        if not hasattr(book, 'bookmark'):
            raise NotExistingExtensionError
        return book.bookmark

    @staticmethod
    def del_bookmark(book, person):
        raise PermissionDeniedError

    @staticmethod
    def search(book, page):
        table = book[len(book)]
        if isinstance(table, PageTableContents):
            return table.search(page)
        raise NotExistingExtensionError

    def read(self, book, page):
        if isinstance(page, str):
            page = self.search(book, page)
        return super().read(book, page)

    def write(self, book, page, text):
        if isinstance(page, str):
            page = AdvancedPerson.search(book, page)
        super().write(book, page, text)


class PageTableContents(Page):
    title = 'TABLE OF CONTENT\n'

    def __init__(self, text=None, max_sign=2000):
        _text = OrderedDict()
        if not text is None:
            lines = text.splitlines()[1:]
            for line in lines:
                chapter, num_page = line.split(':')
                _text[chapter] = num_page
        super().__init__(_text, max_sign)

    def search(self, chapter):
        if chapter in self._text:
            return int(self._text[chapter])
        raise PageNotFoundError

    def __str__(self):
        text = ''.join('{}:{}\n'.format(chapter, num_page) for chapter, num_page in
                       self._text.items())
        return self.title + text

    # переопределяем поведение при вызове функции len
    def __len__(self):
        return len(str(self))

    # перегружаем операторы + и +=
    def __add__(self, other):
        raise PermissionDeniedError

    def __radd__(self, other):
        raise PermissionDeniedError

    def __iadd__(self, other):
        raise PermissionDeniedError


class CalendarBook(Book):
    """"""класс ежедневник с закладкой""""""

    def __init__(self, title, content=None):
        if content is None:
            content, text = CalendarBook.content_generator(int(title))
            super().__init__(title, content)
            self._content.append(PageTableContents(text))
        else:
            super().__init__(title, content)

    @staticmethod
    def content_generator(year):
        content = []
        calendar_ = TextCalendar()
        text = 'TABLE OF CONTENT\n'

        for month in range(1, 13):
            content.append(Page(calendar_.formatmonth(year, month)))
            text += '{}:{}\n'.format(list(month_name)[month], str(len(content)))
            for date in calendar_.itermonthdates(year, month):
                if date.month == month:
                    content.append(Page(date.isoformat()))

        return content, text

    # добавляем закладку
    bookmark = CalendarBookmark('bookmark')

 