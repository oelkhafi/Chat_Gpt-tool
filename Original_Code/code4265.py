import sys

sys.setrecursionlimit(100000)

def isCorrect(index):
    global curval
    if index == -1:
        return True
    if not isCorrect(left[index]):
        return False
    if curval>=value[index]:
        return False
    curval = value[index]
    return isCorrect(right[index])

n = int(input())
if n == 0:
    print('CORRECT')
else:
    value = []
    left = []
    right = []
    curval = -2**31-1
    for i in range(n):
        s = input().split()
        value.append(int(s[0]))
        left.append(int(s[1]))
        right.append(int(s[2]))

    if isCorrect(0):
        print('CORRECT')
    else:
        print('INCORRECT') 