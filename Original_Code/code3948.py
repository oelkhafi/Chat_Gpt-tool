class multifilter:

    def judge_half(pos, neg):
        return pos >= neg

    def judge_all(pos, neg):
        return neg == 0

    def judge_any(pos, neg):
        return pos >= 1

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        fnum = len(self.funcs)
        for i in self.iterable:
            pos = sum(f(i) for f in self.funcs)
            neg = fnum - pos
            if self.judge(pos, neg):
                yield i
 