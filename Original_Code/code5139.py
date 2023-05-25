class AdvancedPerson(Person):
    @staticmethod
    def search(book, name_page):
        if hasattr(book, 'search'):
            return book.search(name_page)
        raise NotExistingExtensionError

    @staticmethod
    def read(book, page):
        page = page if isinstance(page, int) else AdvancedPerson.search(book, page)
        return Person.read(book, page)

    @staticmethod
    def write(book, page, text):
        page = page if isinstance(page, int) else AdvancedPerson.search(book, page)
        Person.write(book, page, text)
        return


class NovelWithTable(Novel):
    """"""класс книга с оглавлением""""""

    def __init__(self, author, year, title, content=None, table=None):
        self.table = table or {}
        super().__init__(author, year, title, content)

    def search(self, chapter):
        if chapter not in self.table:
            raise PageNotFoundError
        return self.table[chapter]

    def add_chapter(self, chapter, page):
        self.table[chapter] = page

    def remove_chapter(self, chapter):
        if chapter in self.table:
            del self.table[chapter]
            return
        raise PageNotFoundError
 