def ab(n, k):        # n - класс 1 - предок класса 2; k - класс 2
    global dct
    return n == k

def lin(n, k):
    global dct
    return n in dct[k]

def lin2(n, k):
    global dct
    global tmp
    tmp.extend(dct[k])
    for i in tmp:
        tmp.extend(dct[i])
    
        
    
dct, tmp = {}, []

lst1 = [[i for i in input().split()] for j in range(int(input()))]
for i in lst1:
    if ':' in i:
        i.remove(':')
    dct[i[0]] = []
    if len(i) > 1:
        for j in range(1, len(i)):
            dct[i[0]].append(i[j])

lst2 = [[i for i in input().split()] for j in range(int(input()))]

for i in lst2:
    lin2(i[0], i[1])
    print('Yes' if ab(i[0], i[1]) or lin(i[0], i[1]) or i[0] in tmp else 'No')
    tmp.clear()



 