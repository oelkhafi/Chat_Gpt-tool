# put your python code here
genom = input()
n = 0
k = []
item = ('', 0)
i = 0
while i < len(genom):
    temp = genom[i]
    while i < len(genom) and genom[i] == temp:
        temp = genom[i]
        n += 1
        i += 1
    item = (temp, n)
    k.append(item)
    n = 0
for i in k:
    print(i[0], i[1], sep='', end='')



 