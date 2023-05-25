# combined solution
from itertools import islice
PRIME_200K = 2750159
THRESHOLD = 50000

cnt = int(input())
ind = list(map(int, input().split()))[:cnt]
end = max(ind)

if end > THRESHOLD:
    # use Erathosthene`s sieve for large lists of primes
    end = PRIME_200K + 1  # 200000th prime number
    sieve = set(range(1, end))
    for p in range(2, int(end**.5)):
        for i in range(p*p, end, p):
            if i in sieve:
                sieve.remove(i)
    pri = sorted(sieve)
else:
    # simple`n`dirty generator for smaller lists of primes
    def prime_gen():
        yield 1; yield 2; yield 3; yield 5
        n = 7
        while 1:
            if n%3 and n%5:
                for d in range(7, int(n**.5)+1):
                    if not n%d:  break
                else:
                    yield n
            n += 2
    pri = list(islice(prime_gen(), end+1))

print(*(pri[i] for i in ind)) 