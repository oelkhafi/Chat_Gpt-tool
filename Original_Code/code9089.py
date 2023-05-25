def binarysch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        guess = (low + high) // 2
        if list[guess] == item:
            return guess + 1
        if list[guess] < item:
            low = guess + 1
        if list[guess] > item:
            high = guess - 1

    return -1


a = list(map(int, input().split()))
n = a.pop(0)

b = list(map(int, input().split()))
k = b.pop(0)

for i in range(k):
    print(binarysch(a, b[i]), end=' ')
 