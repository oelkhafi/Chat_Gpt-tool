class multifilter:
    def judge_any(pos, neg):
        return True if pos >= 1 else False


    def judge_half(pos, neg):
        return True if pos >= neg else False


    def judge_all(pos, neg):
        return True if neg == 0 else False

    
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.prev, self.f, self.j = iterable, funcs, judge
        self.res = []
        for i in self.prev:
            pos = neg = 0
            for j in self.f:
                if j(i):
                    pos += 1
                else:
                    neg += 1
            if self.j(pos, neg):
                self.res.append(i)


    def __iter__(self):
        self.board = 0
        return self


    def __next__(self):
        self.board += 1
        if self.board > len(self.res):
            raise StopIteration
        return self.res[self.board-1] 