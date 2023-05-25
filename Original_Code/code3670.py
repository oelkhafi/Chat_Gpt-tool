import sys

n,m = map(int,sys.stdin.readline().split())
tasks = list(map(int,sys.stdin.readline().split()))
processors = [[0,i] for i in range(n)]

def parent(i):
    return (i - 1) // 2

def leftChild(i):
    return 2 * i + 1

def rightChild(i):
    return 2*i+2

def shiftDown(i):
    minIndex = i
    l = leftChild(i)
    r = rightChild(i)
    if l <= n-1 and processors[l] < processors[minIndex]:
        minIndex = l
    if r <= n-1 and processors[r] < processors[minIndex]:
        minIndex = r

    if i != minIndex:
        temp = processors[i]
        processors[i] = processors[minIndex]
        processors[minIndex] = temp
        shiftDown(minIndex)

for task in tasks:
    print(processors[0][1], processors[0][0])
    processors[0][0] += task
    shiftDown(0) 