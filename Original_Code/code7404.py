import sys


A = [int(i) for i in sys.stdin.readline().strip().split()]
B = [int(i) for i in sys.stdin.readline().strip().split()]
B.pop(0)
answer = []

for b in B:
    left, right = 1, len(A)
    trigger = 0
    m = (left + right) // 2
    while left <= right and left < len(A):
        if b > A[m]:
            left = m + 1
        elif b < A[m]:
            right = m - 1
        elif b == A[m]:
            answer.append(m)
            trigger = 1
            break
        m = (left + right) // 2
    if trigger == 0:
        answer.append(-1)
        
print(*answer) 