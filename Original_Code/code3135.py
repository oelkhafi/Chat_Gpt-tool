n = int(input())
k1 = 0
n1 = n
e = 0
while n1 > 0:
    k1 = k1 + n1 % 10
    n1 = n1 // 10
for i in range(1, n):
    k2 = 0
    i1 = i
    while i1 > 0:
        k2 = k2 + i1 % 10
        i1 = i1 // 10
    if k2 == k1:
        e += 1
        if e == 1:
            print('Найденные числа:')
        print(i)
if e == 0:
    print('Искомых чисел не найдено')
 