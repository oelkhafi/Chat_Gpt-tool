import itertools

def isPrime(n):
        if n in [0, 1]:
                return False
        elif n==2:
                return True
        elif not n & 1:
                return False
        for i in range(3, int(n**0.5)+1, 2):
                if n%i==0:
                        return False
        return True

def primes():
        i = 2
        while True:
                if isPrime(i):
                        yield i
                i += 1
 