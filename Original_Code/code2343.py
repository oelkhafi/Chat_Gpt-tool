class multifilter:
    def judge_half(self):
        return self.pos >= self.neg
    def judge_any(self):
        return self.pos >= 1
    def judge_all(self):
        return self.neg == 0
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable    # - исходная последовательность
        self.funcs = funcs          # - допускающие функции
        self.judge = judge          # - решающая функция
        self.pos, self.neg = (0, 0)
    def reset(self):
        self.pos, self.neg = (0, 0)
    def __iter__(self):
        for element in self.iterable:
            self.reset()
            for func in self.funcs:
                if func(element): self.pos += 1
                else: self.neg += 1
            if self.judge(self): yield element 