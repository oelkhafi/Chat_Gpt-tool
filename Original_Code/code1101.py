import math


def nextPrime(prime, prevPrimes):
    np = prime+1
    while any(map(lambda p: (np % p == 0), prevPrimes)):
        np += 1
        
    return np


def findPrimeFactors(n):
    maxPrimes = math.floor(math.sqrt(n))
    prevPrimes = []
    res = []
    i=2
    while n > 1:
        if n % i == 0:
            res.append(i)
            n = n // i
        else:
            prevPrimes.append(i)
            i = nextPrime(i, prevPrimes)
    return res


n = int(input())
factors = findPrimeFactors(n)
print("" "".join(map(str, factors)))
 