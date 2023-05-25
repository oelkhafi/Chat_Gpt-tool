class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.list = []
        for x in iterable:
            pos = 0
            neg = 0
            for f in funcs:
                if f(x):
                    pos += 1
                else:
                    neg += 1
            if judge(pos, neg):
                self.list.append(x)                

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.list:
            yield i
 