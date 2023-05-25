# put your python code here
a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
    print(a)
    if (b >= c):
        print(c)
        print(b)
    else:
        print(b)
        print(c)
elif (b >= a and b >= c):
    print(b)
    if (a >= c):
        print(c)
        print(a)
    else:
        print(a)
        print(c)
elif (c >= a and c >= b):
    print(c)
    if (a >= b):
        print(b)
        print(a)
    else:
        print(a)
        print(b) 