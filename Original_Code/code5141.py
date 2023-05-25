class CalendarBookmark:
    """"""класс дескриптор - закладка для ежедневника""""""
    def __init__(self):
        self.bookmark = 0

    def __get__(self, obj, obj_type):
        return self.bookmark

    def __set__(self, obj, value):
        if value < 1 or value > len(obj):
            raise PageNotFoundError
        self.bookmark = value


class CalendarBook(Book):

    bookmark = CalendarBookmark()

    def __init__(self, title, content=None):
        super().__init__(title, content)
        self._get_content(int(title))
    
    def _get_content(self, year):
        cal_obj = TextCalendar()
        for month in range(1, 13):
            self._content.append(cal_obj.formatmonth(year, month))
            for date in cal_obj.itermonthdates(year, month):
                if date.month == month:
                    self._content.append(Page(date.isoformat()))
        return self._content 