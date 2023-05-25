def neighbours(i, j):
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if 0 <= row < n and 0 <= col < m:
                if minefield[row][col] != '*':
                    minefield[row][col] += 1


def sapper(n, m, minefield):
    for i in range(n):
        for j in range(m):
            if minefield[i][j] == '*':
                neighbours(i, j)
    print(*[''.join(map(str, minefield[k])) for k in range(n)], sep='\n')


if __name__ == '__main__':
    n, m = map(int, input().split())
    minefield = [[x if x == '*' else 0 for x in input()] for _ in range(n)]
    sapper(n, m, minefield)
 