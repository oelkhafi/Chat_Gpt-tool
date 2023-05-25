def siftup(i):
    if i and a[(i-1)//2] < x:
        a[i] = a[(i-1)//2]
        siftup((i-1) // 2)
    else:
        a[i] = x


def siftdown(i):
    j = i
    a[i] = x
    if 2 * j + 1 <= n and a[i] < a[2*j+1]:
        i = 2 * j + 1
    if 2 * j + 2 <= n and a[i] < a[2*j+2]:
        i = 2 * j + 2
    if j != i:
        a[j] = a[i]
        siftdown(i)


a, n = [], -1
for k in range(int(input())):
    c = input().split()
    if c[0] == 'Insert':
        x = int(c[1])
        a.append(x)
        n += 1
        siftup(n)
    elif c[0] == 'ExtractMax':
        print(a[0])
        x = a.pop()
        n -= 1
        if a:
            siftdown(0)
 