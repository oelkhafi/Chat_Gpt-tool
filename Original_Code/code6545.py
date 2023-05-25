class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = []
        n = len(funcs)
        for x in iterable:
            pos = sum([funcs[i](x) for i in range(n)])
            if judge(pos, n - pos):
                self.iterable.append(x)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            el = self.iterable.pop(0)
        except:
            raise StopIteration
        else:
            return el
 