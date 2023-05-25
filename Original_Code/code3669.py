import sys

size = int(sys.stdin.readline())
H = list(map(int,sys.stdin.readline().split()))

def parent(i):
    return (i - 1) // 2

def leftChild(i):
    return 2 * i + 1

def rightChild(i):
    return 2*i+2

log = []

def shiftDown(i):
    minIndex = i
    l = leftChild(i)
    if l <= size-1 and H[l] < H[minIndex]:
        minIndex = l
    r = rightChild(i)
    if r <= size-1 and H[r] < H[minIndex]:
        minIndex = r
    if i != minIndex:
        log.append([i, minIndex])
        temp = H[i]
        H[i] = H[minIndex]
        H[minIndex] = temp
        shiftDown(minIndex)

for i in range(size, -1, -1):
    shiftDown(i)

print(len(log))
for l in log:
    print(*l)


 