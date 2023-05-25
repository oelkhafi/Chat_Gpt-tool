# put your python code here
matrix = []
matrix_res = []
s = input()
while s != 'end':
    lst = [int(i) for i in s.split()]
    matrix.append(lst)
    s = input()
    matrix_res.append([0]*len(lst))
dim_i = len(matrix)
for i in range(0, dim_i):
    if dim_i == 1:
        i_min = i
        i_max = i
        i_me = i
    else:
        if i == dim_i - 1:
            i_me = i - dim_i
        else:
            i_me = i
        i_max = i_me + 1
        i_min = i_me - 1
    dim_j = len(matrix[i])
    for j in range(0, dim_j):
        if dim_j == 1:
            j_min = j
            j_max = j
            j_me = j
        else:
            if j == dim_j - 1:
                j_me = j - dim_j
            else:
                j_me = j
            j_max = j_me + 1
            j_min = j_me - 1
        bottom = matrix[i_min][j_me]
        top = matrix[i_max][j_me]
        left = matrix[i_me][j_min]
        right = matrix[i_me][j_max]
        matrix_res[i][j] = bottom + top + left + right
for i in matrix_res:
    print(*i)


 