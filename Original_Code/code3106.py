def up(k):
    while k > 0 and a[int((k-1)/2)] < a[k]:
        a[k], a[int((k-1)/2)] = a[int((k-1)/2)], a[k]
        k = int((k-1)/2)

def down(k):
    while 2*k+1 < len(a):
        j = k
        if a[k] < a[2*k+1]:
            j = 2*k+1
        if 2*k+2 < len(a) and a[j] < a[2*k+2]:
            j = 2*k+2
        if j == k:
            break
        else:
            a[k], a[j] = a[j], a[k]
        k = j
            
def insert(elem):
    a.append(elem)
    up(len(a)-1)

def extractmax():
    a[0], a[len(a)-1] = a[len(a)-1], a[0]
    print(a.pop())
    down(0)

n = int(input())
a = []
for i in range(n):
    s = input()
    if s == 'ExtractMax':
        extractmax()
    else:
        t = s.split()
        insert(int(t[1])) 