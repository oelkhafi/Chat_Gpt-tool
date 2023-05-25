class MyOwnSet:
    def __init__(self, iterable=()):
        self._capacity = 8
        self._lenght = 0
        self._storage = [None] * 8
        for w in iterable:
            self.add(w)

    def hash(self, w):
        h = hash(w) % self._capacity
        while True:
            yield h
            h = (h + 1) % self._capacity

    def __len__(self):
        return self._lenght

    def add(self, w):
        for h in self.hash(w):
            if self._storage[h] is None:
                self._storage[h] = w
                self._lenght += 1
                if self._lenght * 4 == self._capacity * 3:
                    self._capacity *= 2
                    self._lenght = 0
                    tmp, self._storage = self._storage, [None] * self._capacity
                    for w in tmp:
                        if w is not None:
                            self.add(w)
                return True
            elif self._storage[h] == w:
                return False

    def discard(self, w):
        for h in self.hash(w):
            if self._storage[h] is None:
                return False
            elif self._storage[h] == w:
                self._storage[h] = None
                self._lenght -= 1
                return True

    def check(self, w):
        for h in self.hash(w):
            if self._storage[h] is None:
                return False
            elif self._storage[h] == w:
                return True


from sys import stdin

myset = MyOwnSet()
d = {""+"": myset.add, ""-"": myset.discard, ""?"": myset.check}
for s in stdin.read().splitlines():
    op, w = s.split()
    print((""FAIL"", ""OK"")[d[op](w)]) 