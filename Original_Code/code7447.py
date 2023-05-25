# put your python code here
b,m = [],0
a = input().split()
if a != []:
    while a[0] != 'end':
        b.append([int(i) for i in a])     
        m += 1
        a = input().split()     
    n = len(b[0])
    if n == 1 and m == 1:
        print(sum(b[0] * 4))
    elif n == 1 and m > 1:
        for i in range(n): 
            for j in range(m): 
                print(sum(b[j]+b[j]+b[j-1]+b[j-m+1]))    
    elif n > 1 and m == 1: 
        b = b[0]
        for i in range(n): 
            print(b[i-1]+b[i-n+1]+b[i]+b[i], end = ' ')
    else:
        for i in range(m): 
            for j in range(n): 
                print(b[i-1][j]+b[i-m+1][j]+b[i][j-1]+b[i][j-n+1], end = ' ')
            print()
 