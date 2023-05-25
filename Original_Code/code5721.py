def fib_mod(n, m):
    f0 = 0
    f1 = 1
    l = [f0, f1]
    for i in range(1, n):
        f0, f1 = f1%m, (f0+f1)%m
        if f0 == 0 and f1 == 1:
            l.pop()
            break
        else:
            l.append(f1)
    return l[n % len(l)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == ""__main__"":
    main() 