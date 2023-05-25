height, width = map(int, input().split())
field = [list(input()) for i in range(height)]
solution = [['.'] * width for j in range(height)]


def get_count(h, w):
    return len(list(filter(lambda x: x == 'X',
                           (field[row][col] for col in ((w - 1) % width, w, (w + 1) % width)
                            for row in ((h - 1) % height, h, (h + 1) % height)))))


for i in range(height):
    for j in range(width):
        if field[i][j] == '.':
            if get_count(i, j) == 3:
                solution[i][j] = 'X'
        else:
            if (get_count(i, j) - 1) in (2, 3):
                solution[i][j] = 'X'

print('\n'.join(''.join(solution[i]) for i in range(height)))
 