class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for e in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                if f(e):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield e 