class Chains():
    def __init__(self, size):
        self._size = size
        self._database = [[] for i in range(size)]
        self.commands = {""add"": self.add, ""find"": self.find,
                         ""check"": self.check, ""del"": self.delete}

    def add(self, arg, _hash):
        if arg not in self._database[_hash]:
            self._database[_hash].append(arg)

    def find(self, arg, _hash):
        print(arg in self._database[_hash] and ""yes"" or ""no"")

    def delete(self, arg, _hash):
        try:
            idx = self._database[_hash].index(arg)
            del self._database[_hash][idx]
        except ValueError:
            pass

    def check(self, arg, _hash):
        print(*self._database[int(arg)][-1::-1])

    def _hash(self, arg):
        degree, _hash, p = 1, 0, 10 ** 9 + 7
        for symbol in arg:
            _hash += (ord(symbol) * degree)
            degree *= 263
        return _hash % p % self._size

    def __call__(self, _string):
        command, arg = _string.split()
        _hash = self._hash(arg)
        self.commands[command](arg, _hash)

if __name__ == ""__main__"":
    database = Chains(int(input()))
    count = int(input())
    for _string in [input() for i in range(count)]:
        database(_string)
 