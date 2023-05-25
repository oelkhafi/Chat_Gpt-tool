a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
if b > a and b >= c:
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
if c > a and c > b:
    print(c)
    if a < b:
        print(a)
        print(b)
    else: 
        print(b)
        print(a) 