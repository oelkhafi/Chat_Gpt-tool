n = int(input())
m = [[0 for _ in range(n)] for _ in range(n)]
m[n//2][n//2] = n ** 2
st, k = 1, 0

for v in range(n//2):
    
    for i in range(n-k):
        m[v][i+v] = st
        st += 1
    
    for i in range(v+1, n-v):
        m[i][-v-1] = st
        st += 1
    
    for i in range(v+1, n-v):
        m[-v-1][-i-1] = st
        st += 1
    
    for i in range(v+1, n-(v+1)):
        m[-i-1][v] = st
        st += 1
    k += 2

for row in m:
    print(*row, sep='\t')
 