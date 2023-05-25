a = [int(i) for i in input().split()]
s = [[0 for i in range(a[1]+2)] for j in range(a[0]+2)]
z = [[0 for i in range(a[1]+2)] for j in range(a[0]+2)]
for i in range(a[0]):
    x = input()
    for j in range(len(x)):
        s[i+1][j+1] = x[j]
s[0] = s[len(s)-2]
s[len(s)-1] = s[1]
for i in range(len(s)):
    s[i][0] = s[i][len(s[i])-2]
    s[i][len(s[i])-1] = s[i][1]
c = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        z[i][j] = s[i][j]
for i in range(1, len(s)-1):
    for j in range(1, len(s[i])-1):
        if s[i-1][j-1] == 'X': c +=1
        if s[i-1][j] == 'X': c +=1
        if s[i-1][j+1] == 'X': c +=1
        if s[i][j-1] == 'X': c +=1
        if s[i][j+1] == 'X': c +=1
        if s[i+1][j-1] == 'X': c +=1
        if s[i+1][j] == 'X': c +=1
        if s[i+1][j+1] == 'X': c +=1
        if s[i][j] == 'X':
            if c == 2 or c == 3:
                z[i][j] = 'X'
            else:
                z[i][j] = '.'
        else:
            if c == 3:
                z[i][j] = 'X'
        c = 0
for i in range(1, len(z)-1):
    for j in range(1, len(z[i])-1):
        print(z[i][j], end = '')
    print()
 