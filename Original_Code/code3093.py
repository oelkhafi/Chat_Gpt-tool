class multifilter():
    def judge_half(pos, neg):
        return True if pos >= neg else False

    def judge_any(pos, neg):
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge = judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                pos, neg = 0, 0
                yield i
 