class multifilter:
    def judge_half(pos, neg):
        # accepts the element, if at least half of the functions accept this element (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # accepts the element, if at least one of the functions accept it (pos >= 1)
        return pos > 0

    def judge_all(pos, neg):
        # accepts the element, if at all functions accept it (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - the original sequence
        # funcs - the allowing functions
        # judge - the judging function
        self.iterable = iterable
        self.funcs = funcs
        self.flen = len(funcs)
        self.judge = judge
        
    def __iter__(self):
        # returns iterator on the resulting sequence
        for x in self.iterable:
            pos = sum(map(lambda f: f(x), self.funcs))
            neg = self.flen - pos
            if self.judge(pos, neg):
                yield x
 