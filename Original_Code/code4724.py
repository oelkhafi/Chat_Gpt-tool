# put your python code here
from bisect import bisect_right as bisect

n = int(input())
array = list(map(int, input().split()))[::-1]
inf = 10 ** 10
d = [inf] * (n + 1)
d[0] = -inf
pos = [0] * (n + 1)
prev = [0] * n

for i in range(n):
    right = bisect(d, array[i])
    if d[right - 1] <= array[i] <= d[right]:
        d[right] = array[i]
        pos[right] = i
        prev[i] = pos[right - 1]

d = [item for item in d if item not in (inf, -inf)]
answer = [0] * len(d)
p = pos[len(d)]
for j in range(len(d)):
    answer[j] = n - p
    p = prev[p]

print(len(d))
print(*answer) 