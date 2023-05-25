class multifilter:
    def judge_half(pos, neg):
        if pos >= neg: return True
        return False

    def judge_any(pos, neg):
        if pos >= 1: return True
        return False

    def judge_all(pos, neg):
        if neg == 0: return True
        return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.source = iterable
        self.filtered = []        
        for item in iterable:
            pos, neg = 0, 0
            for func in funcs:
                if func(item) == True:
                    pos +=1
                else:
                    neg +=1
            if judge(pos,neg) == True:
                self.filtered.append(item)
                
    def __iter__(self):
        for item in self.filtered: yield item 