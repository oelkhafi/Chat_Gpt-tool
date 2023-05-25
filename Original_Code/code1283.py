from collections import Counter
from heapq import heappush, heappop, heapify

 
Z0 = '0'
Z1 = '1'

s = input()
counts = Counter(s)
heap = [[n, [c, '']] for c, n in counts.items()]
heapify(heap)
while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    for e in a[1:]:
        e[1] = Z0 + e[1]
    for e in b[1:]:
        e[1] = Z1 + e[1]
    heappush(heap, [a[0] + b[0]] + a[1:] + b[1:])
code = sorted(heappop(heap)[1:], key=lambda x: (len(x[1]), x))
if len(code) == 1: code[0][1] = Z0
for cz in code:
    s = s.replace(*cz)
print(len(counts), len(s))
for c, z in code:
    print(f'{c}: {z}')
print (s)




 