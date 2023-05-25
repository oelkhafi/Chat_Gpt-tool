# put your python code here
x = 1
b = []
while x != 0:
    a = input()
    if a != 'end':
        a_int = [int(i) for i in a.split()]
        b.append(a_int)
    else:
        x = 0
for i in range(len(b)):
    k = 0
    if i >= len(b) - 1:
        k = i + 1
    for j in range(len(a_int)):
        z = 0
        if j >= len(a_int) - 1:
            z = j + 1
        s = b[i - 1][j] + b[i + 1 - (k)][j] + b[i][j - 1] + b[i][j + 1 - (z)]
        print(s, end=' ')
        s = 0
    print() 