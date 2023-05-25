def num_sum(num):
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
    return s
n = int(input())
s_num = num_sum(n)
p = False
for i in range(n):
    tmp = num_sum(i)
    if tmp == s_num:
        if not p:
            p = True
            print(""Найденные числа:"")
        print(i)
if not p: print('Искомых чисел не найдено')



 