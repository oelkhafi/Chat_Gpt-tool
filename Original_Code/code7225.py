def up(i):
    while i > 0 and a[(i - 1)//2] < a[i]:
        a[(i - 1)//2], a[i] = a[i], a[(i - 1)//2]
        i = (i - 1) // 2

def down(i):
    while 2 * i + 1 <= len(a) - 1:
        j = i
        if a[2 * i + 1] > a[i]:
            j = 2 * i + 1
        if 2 * i + 2 <= len(a) - 1 and a[2 * i + 2] > a[j]:
            j = 2 * i + 2
        if i == j:
            break
        else:
            a[i], a[j] = a[j], a[i]
            i = j

a = []
for _ in range(int(input())):
    s = (input().split())
    if len(s) == 2:
        a.append(int(s[1]))
        up(len(a) - 1)
    else:
        print(a[0])
        a[0] = a[-1]
        a.pop()
        down(0) 