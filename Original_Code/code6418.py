a = []
b = []
s = 0
while True:
    a += [[i for i in input().split()]]
    if a[s] != ['end']:
        s += 1
        continue
    a.remove(['end'])

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])
            
    b=[[0 for j in range(len(a[i]))] for i in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i][j] =(a[i][j+1-len(a[i])] 
                    + a[i][j-1] 
                    + a[i+1-len(a)][j] 
                    + a[i-1][j])
    for i in range(len(a)):
        print(*b[i])
    break 