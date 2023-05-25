# на основе решения
# https://stepik.org/lesson/Итераторы-и-генераторы-24464/step/4?course=Python-основы-и-применение&discussion=337007&thread=solutions
# от Кирилл Скляров
#
# логика фильтрации находится в __init__
# где используется доп. результирующий список self.rslt
# в который добавляются допущенные элементы исходной последовательности
#
# а __next__ просто увеличивает self.index
# и возвращает очередной элемент self.rslt


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0  # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.lst = iterable  # iterable - исходная последовательность
        self.funcs = funcs   # funcs - допускающие функции
        self.judge = judge   # judge - решающая функция
        self.rslt = []       # результирующий список
        self.index = 0       # индекс элемента результирующего списка

        # фильтруем исходную последовательность переданными функциями и получаем результирующий список
        for el in self.lst:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                self.rslt.append(el)

    def __iter__(self):
        return self

    def __next__(self):                       # реализация выдачи следующего элемента:
        if self.index < len(self.rslt):       # пока не достигнем конца результирующего списка
            self.index += 1                   # индек + 1
            return self.rslt[self.index - 1]  # вернём очередной элемент
        else:
            raise StopIteration               # если достигли - кинем исключение 