class multifilter:
    def judge_any(pos, neg):
        return pos > 0

    def judge_half(pos, neg):
        return pos >= neg

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for x in self.iterable:
            # Если у вас есть конкретный элемент, для которого нужно посчитать значения всех функций
            # из какого-то списка (как в нашем случае), то здесь тоже можно использовать
            # генерацию списков:
            # x - элемент, для которого считаем значения
            # functions - список функций
            # тогда список всех значений генерируется следующим образом:
            res = [f(x) for f in self.funcs]
            #дальше остается посчитать, сколько раз встречаются нужные значения - не заводить счетчики,
            # а воспользоваться методом count() для списка.
            if self.judge(res.count(True),res.count(False)): yield x 