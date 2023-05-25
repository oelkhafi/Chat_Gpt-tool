def isZeroRow(m, row):
    """""" (int, [m]) => boolean
      check if row with length m consists of only zeros
    """"""
    for i in range(m):
        if row[i] != 0:
            return False
    return True


def findNotZeroIndex(n, a, fromIdx):
    """""" (int, [[int]]) => int
        find not zero item from a[fromIdx][fromIdx]
        to a[len(a)][fromIdx]
        if found return index
        if did not find return -1
    """"""
    n = len(a)
    for i in range(fromIdx+1,n):
        if a[i][fromIdx] != 0:
            return i
    return -1


def makeDiagonalMatrix(n, m, a):
    """""" (int, int, [n, m]) => [n, m]
        Make matrix with zeros below the main diagonal.
    """"""
    for i in range(min(n, m)):
        startCol = i
        while startCol < m and a[i][startCol] == 0:
            # try to find not zero factor, and swap
            # with current row
            notZeroIdx = findNotZeroIndex(n, a, i)
            if notZeroIdx != -1:
                # swap two rows
                a[i], a[notZeroIdx] = a[notZeroIdx], a[i]
                break
            # all rows with zero factors
            # step to the right to find column without zeros
            startCol += 1

        if startCol == m:
            return a
        
        ai = a[i]
        for j in range(i+1, n):
            aj = a[j]
            k = aj[startCol] / ai[startCol]
            for idx in range(startCol, m+1):
                aj[idx] -= k * ai[idx]
            a[j][i] = 0
    return a


def solveGauss(n, m, a):
    """"""    
        find solve of the linear system of equations
        by Gauss way.
        Return tuple:
        first - string:
         ""YES"" - there is a solvation;
         ""NO"" - there is not a solvation;
         ""INF"" - infinit number of solvations.
        second - list:
         if first is ""YES"", then contains roots;
         else it is None
    """""" 
    if n == 0 or m == 0:
        return (""NO"", None)
    if n == 1 and m == 1:
        if a[0][0] == 0:
            return (""NO"", None)
        return (""YES"", [a[0][1]/a[0][0]])
    
    makeDiagonalMatrix(n, m, a)
    # remove row with all zeros
    rowsIndicesToDelete = []
    for i in range(n):
        if isZeroRow(m, a[i]):
            if a[i][m] == 0:
                # we need to remove this row
                rowsIndicesToDelete.append(a[i])
            else:
                # there are not an equation solvation
                return (""NO"", None)
    if rowsIndicesToDelete:
        for row in rowsIndicesToDelete:
            del row
        n -= len(rowsIndicesToDelete)
    if n < m:
        return (""INF"", None)
    
    res = [0] * m
    for i in range(n-1,-1,-1):
        # compute x_i
        if a[i][i] == 0:
            raise Exception(""ZERO"" + str(i), a)
        
        res[i] = a[i][m] / a[i][i]
        # change equation above by substract x_i from b
        for j in range(i):
            a[j][m] -= res[i] * a[j][i]
    return (""YES"", res)

            
n, m = map(int, input().split())
a = []
for _ in range(n):
    m1 = list(map(float, input().split()))
    a.append(m1)

message, res = solveGauss(n, m, a)
print(message)
if message == 'YES':
    print("" "".join(map(str, res)))
 