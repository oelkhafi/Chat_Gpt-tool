def num_neib(ind_i, ind_j, mx):
    res = 0
    for i in range(ind_i - 1, ind_i + 2):
        if i <0  or i > n-1: continue
        else:
            for j in range(ind_j - 1, ind_j + 2):
                if (i == ind_i and j == ind_j) or j < 0 or j > m-1: continue
                else:
                    if mx[i][j] == '*': res += 1
    return res
n, m = map(int, input().split())
mx = []
for _ in range(n):
    mx.append(input())
solved_mx = []
for i in range(n):
    solved_mx.append('')
    for j in range(m):
        if mx[i][j] == '*': solved_mx[i] += '*'
        else: solved_mx[i] += str(num_neib(i, j, mx))
for row in solved_mx: print(row) 