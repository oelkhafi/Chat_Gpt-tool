class multifilter:
    def judge_half(self, pos, neg):
        return pos >= neg
        
    def judge_any(self, pos, neg):
        return pos >= 1

    def judge_all(self, pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        res = []
        for el in self.iterable:
            pos = 0
            for func in self.funcs:
                if func(el): pos += 1
            neg = len(self.funcs) - pos
            if self.judge(self, pos, neg): yield el 