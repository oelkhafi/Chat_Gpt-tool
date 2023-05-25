from collections import Counter
import heapq
from operator import itemgetter

st = input()
heap = []
c = Counter(st)
frequencies = c.most_common()
for f in frequencies:
    v = (f[1], f[0])
    heapq.heappush(heap, v)

tree = {}
while len(heap) > 1:
    v1 = heapq.heappop(heap)
    v2 = heapq.heappop(heap)
    priority = v1[0] + v2[0]
    value = v1[1] + v2[1]
    heapq.heappush(heap, (priority, value))
    tree[value] = (v1[1], v2[1])


root = heapq.heappop(heap)[1]
q = [(root, '')]
if len(tree) == 0:
    tree[root] = None
    q = [(root, '0')]

code_table = {}
while len(q):
    next_key, prefix_code = q.pop()
    next = tree.get(next_key, None)
    if next:
        q.append((next[0], prefix_code + '0'))
        q.append((next[1], prefix_code + '1'))
    else:
        code_table[next_key] = prefix_code

encoded = ''
for ch in st:
    encoded += code_table[ch]

print(len(code_table), len(encoded))
for ch, code in sorted(list(code_table.items()),key=itemgetter(0)):
    print(ch + ':', code)

print(encoded)
 