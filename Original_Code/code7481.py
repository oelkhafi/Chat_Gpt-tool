def fib_digit(n):
    if n<=1:
        return 1
    else:
        a = 0
        b = 1
        c = 1
        for i in range(2, n):
            a = b
            b = c
            c = (b + a)%10
        return c


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == ""__main__"":
    main() 