def inv(a, acc=0):
    b = []
    for k in range(len(a) // 2):
        b.append([])
        i = 0
        j = 0
        while i < len(a[2*k]) and j < len(a[2*k+1]):
            if a[2*k][i] <= a[2*k+1][j]:
                b[-1].append(a[2*k][i])
                i += 1
            else:
                b[-1].append(a[2*k+1][j])
                j += 1
                acc += len(a[2*k]) - i
        for ii in range(i, len(a[2*k])):
            b[-1].append(a[2*k][ii])
        for jj in range(j, len(a[2*k+1])):
            b[-1].append(a[2*k+1][jj])
    if len(a) % 2 == 1:
        b.append(a[-1])
    if len(b) == 1:
        return acc
    else:
        return inv(b, acc)


input()
print(inv([[int(i)] for i in input().split()]))
 