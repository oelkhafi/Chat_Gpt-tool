def binary_search(lst, x):
    l, r = 0, len(lst) - 1
    while l <= r:
        m = l + (r - l) // 2
        if lst[m] == x:
            return m + 1      # Порядок вывода от 1, а не от 0
        elif lst[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1


def main():
    a = [int(i) for i in input().split()][1:]
    b = [int(i) for i in input().split()][1:]
    for j in b:
        print(binary_search(a, j), end=' ')


if __name__ == '__main__':
    main()
 