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
        self.index = 0
        self.length = len(iterable)

    def __next__(self):
        while True:
            if self.index < self.length:
                el = self.iterable[self.index]
                pos = 0
                neg = 0
                self.index += 1
                for func in self.funcs:
                    if func(el):
                        pos += 1
                    else:
                        neg += 1
                if self.judge(pos, neg):
                    return el
            else:
                raise StopIteration

    def __iter__(self):
        return self 