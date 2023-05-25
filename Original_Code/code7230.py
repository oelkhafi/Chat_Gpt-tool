import sys


def lisbuttonup(a):
    d = [1] * len(a)
    for i in range (len(a)):
        for j in range(i):
            if d[j] + 1 > d[i] and not a[i] % a[j]:
                d[i] = d[j] + 1
    return max(d)


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n = next(reader)
    lst = next(reader)
    print(lisbuttonup(lst))


if __name__ == '__main__':
    main()
 