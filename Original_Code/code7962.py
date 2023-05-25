# put your python code here
n = int(input())
a = 0
b = 0
c = 0
d = 0
for i in range(1,n+1):
    x = int(input())
    if x == 2:
        d += 1
    elif x == 3:
        c += 1
    elif x == 4:
        b += 1
    elif x == 5:
        a += 1
print(d, c, b, a)    



 