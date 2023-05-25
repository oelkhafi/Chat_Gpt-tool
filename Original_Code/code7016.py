from sys import stdin
read = lambda: map(int, stdin.readline().split())
n_cuts, n_dots = read()
heap = []
for i in range(n_cuts):
    lx, rx = read()
    if lx <= rx:
        heap.append((lx, -1, i))
        heap.append((rx, 1, -i))
for i, dx in enumerate(read()):
    heap.append((dx, 0, i))
assert i+1 == n_dots
hits = [0] * n_dots
heap.sort()
depth = 0
for x, etype, i in heap:
    if etype == 0:
        hits[i] = depth
    elif etype < 0:
        depth += 1
    else:
        depth -= 1
print(*hits) 