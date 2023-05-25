class multifilter:
    def judge_half(pos, neg):
        if pos>=neg:
            return True# допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True# допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True# допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable# iterable - исходная последовательность
        self.funcs = funcs# funcs - допускающие функции
        self.judge = judge# judge - решающая функция

    def __iter__(self):
        for item in self.iterable:
            self.pos = 0
            self.neg = 0
            for f in self.funcs:
                if f(item):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos,self.neg):
                yield item# возвращает итератор по результирующей последовательности

 