def numerics(n):
    return [n // 1000,
            (n % 1000) // 100,
            (n % 100) // 10,
             n % 10]

def kaprekar_step(L):
    min_n = sorted(L)
    max_n = min_n[::-1]
    powers = map(lambda x: 10**x, range(len(L)-1, -1, -1))
    return sum(map(lambda t: (t[0] - t[1]) * t[2], zip(max_n, min_n, powers)))

def kaprekar_loop(n, f=print):
    def kgen(n):
        yield n
        while n != 6174:
            n = kaprekar_step(numerics(n))
            yield n
    any(map(f, kgen(n)))
                
 