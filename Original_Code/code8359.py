# на основе решения
# https://stepik.org/lesson/Итераторы-и-генераторы-24464/step/4?course=Python-основы-и-применение&discussion=334958&thread=solutions
# от Anonymous 19317501
#
# логика фильтрации находится в __next__
# где в цикле пробегаемся по исходной последовательности
# каждый элемент которой просеивается через функции-фильтры
# и возвращается допущенный элемент
# а после окончания цикла поднимается исключение
# окончания итерации


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
        self.index = 0       # индекс элемента последовательности self.lst

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lst):
            pos, neg = 0, 0
            for func in self.funcs:
                if func(self.lst[self.index]):
                    pos += 1
                else:
                    neg += 1
            self.index += 1
            if self.judge(pos, neg):
                return self.lst[self.index - 1]
        raise StopIteration 