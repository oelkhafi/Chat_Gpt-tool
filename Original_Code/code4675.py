def next_state(row, col):
    live_neighbors = 0
    for i in range(3):
        for j in range(3):
            """""" Пропускаем саму ячейку """"""
            if i == 1 and j == 1:
                continue
            if cells[(row - 1 + i) % height][(col - 1 + j) % width] == 'X':
                live_neighbors += 1
    if cells[row][col] == '.' and live_neighbors == 3:
        return 'X'
    if cells[row][col] == 'X' and live_neighbors not in (2, 3):
            return '.'
    return cells[row][col]


height, width = map(int, input().split())
cells = tuple(tuple(input()) for _ in range(height))
cells_next_state = [[0] * width for _ in range(height)]
for i in range(height):
    for j in range(width):
        cells_next_state[i][j] = next_state(i, j)
print('\n'.join((''.join(line) for line in cells_next_state))) 