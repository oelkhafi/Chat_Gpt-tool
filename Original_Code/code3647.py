class multifilter:
    def judge_half(pos, neg):
        if pos >= neg: return True
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1: return True

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0: return True

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self
    
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.result = []
        self.i = -1
        for x in self.iterable:
            pos, neg = 0,0
            for f in self.funcs:
                if f(x): pos += 1
                else: neg += 1
            if self.judge(pos, neg): self.result.append(x)        

    def __next__(self):
        if self.i < len(self.result)-1:
            self.i += 1
            return self.result[self.i]
        else:
            raise StopIteration
 