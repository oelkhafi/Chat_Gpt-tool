n = int(input())
n1 = n
s = 0
q = 0
o = True
while n != 0:
    s += n % 10
    n //= 10
for i in range (0, n1):
    s1, w = 0, i
    while w != 0:
        s1 += w % 10
        w //= 10
    if s1 == s:
        if o:
            print('Найденные числа:')
            o = False
        print(i)
        q += 1
if q == 0:
    print('Искомых чисел не найдено') 