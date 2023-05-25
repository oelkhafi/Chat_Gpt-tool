def add_koeff_rows(i, k, j, mx):
    '''add j-th row of matrix multiplying on koefficient k to i-th row of matrix'''
    mx[i][:] = [mx[i][_] + k * mx[j][_] for _ in range(len(mx[j]))]

def sort(k, mx):
    """"""sorted under-matrix from position [k,k] reversed""""""
    m =[]
    for i in range(k, len(mx)):
        m.append(mx[i][:])
    m.sort(key = lambda x: abs(x[k]), reverse=True)
    for i in range(k, len(mx)):
        mx[i][:] = m[i-k][:]

def remove_0_rows(mx):
    i = 0
    while i<len(mx):
        if sum(mx[i]) == 0:
            del mx[i]
            if i == len(mx): break
            else: continue
        else: i += 1

def is_solving(mx):
    for row in mx:
        if list(filter(lambda x: x!=0, row[:-1])) == []: return 'NO'
    if len(mx) > 0:
        if len(mx) < len(mx[0])-1: return 'INF'
    return 'YES'

def main():
    n, m = map(int, input().split())
    
    T = []
    for _ in range(n):
        T.append(list(map(int, input().split())))
    
#go ahead
    if n>1:
        sort(0, T)
        add_koeff_rows(1, -T[1][0] / T[0][0], 0, T)
    for i in range(n-1):
        if i == m: break
        sort(i+1, T)
        if T[i][i] != 0:
            for j in range(i+1, n):
                add_koeff_rows(j, -T[j][i]/T[i][i], i, T)
                
# backward                
    for i in range(n-1, 0, -1):
        if i > m: continue 
        if T[i][i] != 0:
            for j in range(i-1, -1, -1):
                add_koeff_rows(j, -T[j][i] / T[i][i], i, T)

# define solving
    remove_0_rows(T)
    ans = is_solving(T)
    if ans == 'YES':
        if sum([T[i][m]/T[i][i] for i in range(m)]) == 0: ans = 'NO'
    print(ans)
    if ans == 'YES':
        print(' '.join(map(str,[T[i][m]/T[i][i] for i in range(m)])))

if __name__ == ""__main__"": main() 