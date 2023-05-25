# собственное решение через yield (вместо __next__)
#
# логика работы прописана в итераторе объекта __iter__
# где пробегаемся по элементам исходной последовательности
# просеиваем элемент через функции-фильтры
# и если выбранная функция judge дала добро
# то yield`им этот элемент
#
#
#


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

    def __iter__(self):
        for el in self.lst:
            pos, neg = 0, 0
            for f in self.funcs:
                pass
                if f(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el 