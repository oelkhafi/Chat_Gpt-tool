def fib_mod(n, m):
    if n<1:
        return 0
    else:
        a = 0
        b = 1
        for i in range(n):
            a, b = b, (a + b) % m
            if a == 0 and b == 1:
                a = 0
                b = 1
                k=n%(i+1)
                if k>1:
                    for i in range(k-1):
                        a, b = b, (a + b) % m
                    return b
                else:
                    return k
                break
    return a


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == ""__main__"":
    main() 