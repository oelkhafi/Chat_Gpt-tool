n = int(input())
a = [[0] * n for i in range(n)]
x = n - 1
y = n - 1
b = 0
r = 1

while x > 0:
    for i in range(x):
        a[b][b + i] = r
        r += 1
    for i in range(x):
        a[b + i][y] = r
        r += 1
    for i in range(x):
        a[y][(-i - 1) - b] = r
        r += 1
    for i in range(x):
        a[(-i - 1) - b][b] = r
        r += 1
    b += 1
    x -= 2
    y -= 1

if n % 2 != 0:
    a[-1 - (n // 2)][-1 - (n // 2)] = n ** 2

for i in a:
    for j in i:
        print(j, end=' ')
    print()
 