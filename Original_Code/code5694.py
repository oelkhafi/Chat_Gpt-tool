import copy
a = []
b = input().split()

while b != [""end""]:
    a.append(b)
    b = input().split()

c = copy.deepcopy(a)

for row in range(0, len(a)):
    for col in range(0, len(a[0])):
        c[row][col] = int(a[row][col - len(a[0]) + 1]) + int(a[row][col - 1]) + int(a[row - len(a) + 1][col]) + int(a[row - 1][col])

for row in range(0, len(a)):
    for col in range(0, len(a[0])):
        print(c[row][col], end="" "")
    print()



 