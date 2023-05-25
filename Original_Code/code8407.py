from array import array
q = array('Q') # unsigned long long
N = 0

def siftDown(index):
    child1Index, child2Index = index * 2 + 1, index * 2 + 2
    maxIndex = index
    if child2Index < N:
        if q[child2Index] > q[maxIndex]:
            maxIndex = child2Index 
    if child1Index < N:
        if q[child1Index] > q[maxIndex]:
            maxIndex = child1Index
    if maxIndex != index:
        q[index], q[maxIndex] = q[maxIndex], q[index]
        siftDown(maxIndex)
        
def siftUp(index):
    parentIndex = (index - 1) // 2
    if parentIndex >= 0 and q[parentIndex] < q[index]:
        q[parentIndex], q[index] = q[index], q[parentIndex]
        siftUp(parentIndex)
        
def insert(x):
    global N
    q.append(x)
    siftUp(N)
    N += 1

def extractMax():
    global N
    print(q[0])
    q[0] = q[N - 1]
    q.pop()
    N -= 1
    siftDown(0)

for i in range(int(input())):
    command = input()
    if command[0] == 'I':
        insert(int(command.split(' ')[1]))
    else: 
        extractMax()
 