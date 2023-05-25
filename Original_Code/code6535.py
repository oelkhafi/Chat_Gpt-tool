import sys

s1, s2 = list([ch for ch in line.strip()] for line in sys.stdin)
n, m = len(s1) + 1, len(s2) + 1

opt_arr = [[0 for i in range(n)] for j in range(m)]

for raw in range(m):
    for column in range(n):
        if raw == 0 or column == 0:
            opt_arr[raw][column] = raw + column
        else:            
            current = min(opt_arr[raw-1][column-1], opt_arr[raw-1][column], opt_arr[raw][column-1])            
            if current == opt_arr[raw-1][column-1] and s1[column-1] == s2[raw-1]:
                opt_arr[raw][column] = current
            else:
                opt_arr[raw][column] = current + 1
            
print(opt_arr[m-1][n-1])

""""""
def print_matrix(arr):
    for i in arr:
        print(*i)

print_matrix(opt_arr)
print("""")

raw, column = m-1, n-1
out1 = """"
out2 = """"
while raw > 0 and column > 0:   
    cur = min(opt_arr[raw][column-1], opt_arr[raw-1][column-1], opt_arr[raw-1][column])
    if cur == opt_arr[raw-1][column-1]:
        out1 += s1[column-1]
        out2 += s2[raw-1]
        opt_arr[raw][column] = ""#""
        raw -= 1
        column -= 1
    elif cur == opt_arr[raw-1][column]:
        out1 += '_'
        out2 += s2[raw-1]
        opt_arr[raw][column] = ""#""
        raw -= 1
    elif cur == opt_arr[raw][column-1]:
        out1 += s1[column-1]
        out2 += '*'
        opt_arr[raw][column] = ""#""
        column -= 1
    else:
        print(""WTF"")

while raw > 0:
    opt_arr[raw][column] = ""#""
    out1 += '_'
    out2 += s2[raw-1]
    raw -= 1
while column > 0:
    opt_arr[raw][column] = ""#""
    out1 += s1[column-1]
    out2 += '*'
    column -= 1
opt_arr[raw][column] = '#'    

print_matrix(opt_arr)
print(out1[::-1], out2[::-1], sep = ""\n"")
"""""" 