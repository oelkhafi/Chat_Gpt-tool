m = []
n = []
d = 0
i = ''
#ввод произвольной матрицы
while i != ""end"": 
    for i in [j for j in input().split()]:
        if i != ""end"":
            n.append(int(i))
            d = n.copy()
    if i != ""end"":
        m.append(d)
        n.clear()

#обработка
for i in range(len(m)):
    n.clear()
    for j in range(len(m[0])):
        d = m[i-1][j] + m[i][j-1] + m[(i+1)%len(m)][j] + m[i][(j+1)%len(m[0])]
        n.append(d)
    for k in n:
        print(k,end="" "")
    print()



 