from sys import stdin


def editing_distance():
    a, b = [line[:-1] for line in stdin.readlines()]
    a_, b_ = len(a) + 1, len(b) + 1
    d = [[0 for _ in range(b_)] for _ in range(a_)]
    for i in range(a_):
        d[i][0] = i
    for j in range(b_):
        d[0][j] = j
    for i in range(1, a_):
        for j in range(1, b_):
            c = int(a[i - 1] != b[j - 1])
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + c
                          )
    print(d[-1][-1])


if __name__ == '__main__':
    editing_distance()
 