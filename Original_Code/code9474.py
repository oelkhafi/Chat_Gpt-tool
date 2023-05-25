class multifilter:
    def judge_half(pos, neg):
        """"""допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)""""""
        return pos >= neg


    def judge_any(pos, neg):
        """"""допускает элемент, если его допускает хотя бы одна функция (pos >= 1)""""""
        return pos >= 1


    def judge_all(pos, neg):
        """"""допускает элемент, если его допускают все функции (neg == 0)""""""
        return neg == 0


    def __init__(self, iterable, *funcs, judge=judge_any):
        """"""    iterable - исходная последовательность
    funcs - допускающие функции
    judge - решающая функция""""""
        self.judge = judge
        self.num = 0
        self.iterable = iterable
        self.funcs = funcs


    def __iter__(self):
        """""" возвращает итератор по результирующей последовательности""""""
        return self

    def __next__(self):
        while self.num < len(self.iterable):
            val = self.iterable[self.num]
            valfilter = [func(val) for func in self.funcs]
            pos = valfilter.count(True)
            neg = len(valfilter) - pos
            self.num += 1
            if self.judge(pos,neg):
                return val
        raise StopIteration
 