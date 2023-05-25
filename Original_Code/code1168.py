def denom(x):
    return x % 1000000007

def fastPow(a, p):
    if p == 1:
        return a
    t = fastPow(a, p // 2)
    t = denom(t * t)
    if p & 0x1:    
        return denom(t * a)
    else:
        return t
    
def fastDivision(a, b):
    ''' (int, int) => int
        Fast computation of denom(a // b).
        It is equal to denom(a * b^1000000005) '''
    return denom(a * fastPow(b, 1000000005))

def catalan(n):
    cn = 1 # C_0 = 1
    for k in range(1, n+1):
        newCn = denom(2 * cn)
        newCn = denom((2 * k - 1) * newCn)
        cn = fastDivision(newCn, k+1)
    return cn

n = int(input())
print(catalan(n)) 