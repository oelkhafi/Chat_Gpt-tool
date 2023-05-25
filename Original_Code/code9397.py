class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable   # исходная последовательность
        self.funcs = funcs         # допускающие функции
        self.judge = judge         # решающая функция
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.i < len(self.iterable):
                self.i += 1
                
                x, pos, neg = self.iterable[self.i - 1], 0, 0
                for func in self.funcs:
                    if func(x):
                        pos += 1
                    else:
                        neg += 1
                
                if self.judge(pos, neg):
                    return x
            else:
                raise StopIteration 