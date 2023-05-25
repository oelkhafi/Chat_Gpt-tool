def condition(r):
    return r % 1 == 0 and 1000 > r > 0


# if a == 0
def quadratic_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a != 0:
        x1 = (-b + discr ** .5) / (2 * a)
        x2 = (-b - discr ** .5) / (2 * a)
        return x1, x2
    if b != 0:
        return -c / b,
    else:
        return ()


# if a != 0
def cubic_roots(a, b, c, d):
    roots = []

    def add_root(r):
        if condition(r):
            if a * (r ** 3) + b * (r ** 2) + c * r + d == 0:
                roots.append(r)

    a_factors = list(find_factors(a))
    d_factors = list(find_factors(d))
    for f in a_factors + d_factors:
        add_root(f)
    for af in a_factors:
        for df in d_factors:
            add_root(af / df)
    return roots


def find_factors(n):
    if n < 0:
        n = -n
    for i in range(1, int(n ** .5 + 1)):
        if n % i == 0:
            yield i
            if i ** 2 != n:
                yield n / i


def find_roots(a, b, c, d):
    if a == 0:
        return quadratic_roots(b, c, d)
    if d == 0:
        return quadratic_roots(a, b, c)
    else:
        return cubic_roots(a, b, c, d)


roots = find_roots(*(int(input()) for _ in range(4)))
sorted_roots = sorted(filter(lambda x: condition(x), set(roots)))
if sorted_roots:
    print(*map(int, sorted_roots), sep='\n')
 