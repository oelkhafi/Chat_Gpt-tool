def neighbours(i, j, result):
    for p in range(i - 1, i + 2):
        if 0 <= p < n:
            for q in range(j - 1, j + 2):
                if 0 <= q < m:
                    if field[p][q] == '*':
                        result[p][q] = '*'
                    elif result[p][q] != '*':
                        result[p][q] += 1


def wiper(n, m, field):
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                neighbours(i, j, result)
    print(*[''.join(map(str, result[k])) for k in range(n)], sep='\n')


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = [[x for x in input()] for _ in range(n)]
    wiper(n, m, field)
 