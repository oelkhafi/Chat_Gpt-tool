# put your python code here
from collections import deque


class Deque(deque):
    def pop(self, *args, **kwargs):
        if super(Deque, self).__len__() > 0:
            return super(Deque, self).pop()
        return -1

    def popleft(self, *args, **kwargs):
        if super(Deque, self).__len__() > 0:
            return super(Deque, self).popleft()
        return -1


d = Deque()
operations = [d.append, d.pop, d.appendleft, d.popleft]
for _ in range(int(input())):
    op, value = map(int, input().split())
    if op in (1, 3):
        operations[op - 1](value)
    if op in (2, 4) and value != operations[op - 1]():
        print('NO')
        break
else:
    print('YES') 