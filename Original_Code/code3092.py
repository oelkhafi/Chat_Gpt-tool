def antifoo(x):
    global dct
    global tst
    for i in dct:
        if x in dct[i]:
            tst.add(i)
            antifoo(i)

    
dct, tst = {}, set()
n = [[i for i in input().split()] for j in range(int(input()))]
for i in n:
    if ':' in i:
        i.remove(':')
    if len(i) > 1:
        top = i.pop(0)
        dct[top] = []
        dct[top].extend(i)
    else:
        dct[i[0]] = []
k = [input() for i in range(int(input()))]

for i in k:
    antifoo(i)
    if i in tst:
        print(i)
 