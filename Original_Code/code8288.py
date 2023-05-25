a = [int(i) for i in input().split()]
b = 0
c = (len(a) - 2)
for i in a:
    if len(a) == 1:
        print(a[0])
        break
    print(a[1] + a[-1], end=' ')
    while c != 0:
        print(a[b] + a[b+2], end=' ')
        b += 1
        c -= 1
    print(a[-2] + a[0], end=' ')
    break


        
        


 