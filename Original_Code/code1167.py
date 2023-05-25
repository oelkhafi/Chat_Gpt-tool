def makePrimeResidueFunc(p):
    """""" (int) => ((int) => int)
        Return function which compute residue
        of a number to the modulus p.
        p has to b a prime number. """"""
    return lambda x: x % p


def catalan(n):
    """""" Compute n-th Catalan number. """"""
    prf = makePrimeResidueFunc(1000000007)
    # Find all Catalan number less and equal
    # the n and store them in the cache.
    cCache = [0] * (n+1)
    cCache[0] = 1 # C_0 == 1
    for i in range(1, n+1):
        for k in range(1, i+1):
            s = prf(cCache[k-1] * cCache[i-k])
            cCache[i] = prf(cCache[i] + s)
    return cCache[n]


print(catalan(int(input()))) 