import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    assert len(a) == n
    d = [0] * n
    for i in range(n):
        d[i] = 1
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])
    return ans


if __name__ == '__main__':
    print(main())
 