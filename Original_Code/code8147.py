n = int(input())
c = 0
if n == 2:
    print(""1"")
else:
    for i in range(4, n+1):
        d = 2
        while d * d <= i and i % d != 0:
            d += 1
        e = d * d > i
        if e == True:
            c = c + 1

    print(c+2)






 