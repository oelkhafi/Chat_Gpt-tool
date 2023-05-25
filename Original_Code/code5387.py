import math


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def primes():
    i = 2
    is_prime = True

    while True:
        border = math.floor(math.sqrt(i))

        for j in range(2, border + 1):
            if gcd(i, j) != 1:
                is_prime = False
                break
        else:
            yield i

        i += 1 