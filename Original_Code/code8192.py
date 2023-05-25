import heapq, math

h = []
def heap_pop():
    return -heapq.heappop(h)
def heap_push(x):
    heapq.heappush(h, -x)
def heap_top():
    return -h[0]

n = input()
h = [-int(x) for x in input().split()]
capacity = int(input())
heapq.heapify(h)
moves = 0
while len(h) > 0:
    loaded = [heap_pop()]
    while len(h) > 0 and (sum(loaded) + heap_top()) <= capacity:
        loaded.append(heap_pop())
    for fruit in loaded:
        if fruit > 1:
            heap_push(fruit - math.ceil(fruit / 2))
    moves += 1

print(moves) 