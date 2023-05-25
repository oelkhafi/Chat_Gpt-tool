# put your python code here
mx = []
n, m = 0, 0
while True:
    line = input()
    if line == 'end':
        m = len(mx[0])
        break
    else:
        mx.append([int(i) for i in line.split()])
    n += 1
i = 3

def sumneib(mx, i, j):
    n = len(mx)
    m = len(mx[0])
    if n == 1 and m == 1:
        return mx[i][j] * 4
    elif n == 1:
        return mx[i][j] * 2 + mx[i][j+1 if j < m-1 else 0] + mx[i][j-1 if j>0 else m-1]
    elif m == 1:
        return mx[i+1 if i < n-1 else 0][j] + mx[i-1 if i>0 else n-1][j] + mx[i][j] * 2
    else:
        return mx[i+1 if i < n-1 else 0][j] + mx[i-1 if i>0 else n-1][j] + mx[i][j+1 if j < m-1 else 0] + \
            mx[i][j-1 if j>0 else m-1]

m1 = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        m1[i][j] = sumneib(mx, i, j)
        
print('\n'.join([' '.join([str(el) for el in row]) for row in m1])) 