class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        #self.pos = pos
        #self.neg = neg
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        #self.pos = pos
        #self.neg = neg
        if pos >= 1:
            return True

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        #self.pos = pos
        #self.neg = neg
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge = judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for x in self.iterable:
            self.pos = 0
            self.neg = 0
            for foo in self.funcs:
                res = foo(x)

                if res is True:
                    self.pos += 1
                else:
                    self.neg += 1

            c = self.judge(self.pos, self.neg)
            if c is True:
                yield x 