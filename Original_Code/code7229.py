def countsort(a):
    b, c = [0] * 11, [0] * len(a)
    for i in a:
        b[i] += 1
    for i in range(1, 11):
        b[i] += b[i - 1]
    for j in a[::-1]:
        c[b[j] - 1] = j
        b[j] -= 1
    return c


def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(*countsort(lst))


if __name__ == '__main__':
    main()
 