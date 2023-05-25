lstIn = []
lstIn.append(int(input()))

lstOut = []
temp = lstIn[0]

while temp != 0: 
    a = int(input())
    temp += a
    lstIn.append(a)

for el in lstIn:
    lstOut.append(el * el)

temp = 0

for el in lstOut:
    temp += el

print(temp)


 