import sys


def stairs(a, n):
    prev, curr, acc = 0, a[1], a[1]
    for i in range(2, n + 1):
        acc = max(prev, curr) + a[i]
        prev, curr = curr, acc
    return acc

#  итерация
#def stairs(a, n):
#    d = [0] + [a[1]] + [0] * (n - 1)
#    for i in range(2, n + 1):
#        d[i] = max(d[i - 1], d[i - 2]) + a[i]
#    return d[-1]

#  рекурсия - не прошла
#def stairs(a, n):
#    if n < 2:
#        return a[n]
#    return max(stairs(a, n - 1), stairs(a, n - 2)) + a[n]


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, = next(reader)
    step_price = [0] + list(next(reader))
    print(stairs(step_price, n))


if __name__ == '__main__':
    main()
 