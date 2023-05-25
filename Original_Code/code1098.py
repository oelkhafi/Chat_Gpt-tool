from functools import reduce


def printBoard(strings):
    for line in strings:
        res = reduce(lambda x,y: x+str(y), line, """").strip()
        print(res)


def addOne(board, x, y):
    cnt = 0
    n = len(board)
    m = len(board[0])
    for dy in range(-1,2):
        cy = y + dy
        if cy < 0 or cy >= n:
            continue
        for dx in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            cx = x + dx
            if cx < 0 or cx >= m:
                continue
            val = board[cy][cx]
            if val != ""*"":
                board[cy][cx] = val + 1
                
    return cnt

def getSolve(strings):
    board = [list(line) for line in strings]
    board = list(map(lambda line: list(map(lambda x: x if x==""*"" else 0, line)), board))
    n = len(board)
    if n == 0:
        return strings
    
    m = len(board[0])
    for y in range(n):
        for x in range(m):
            if board[y][x] == ""*"":
                addOne(board, x, y)
    return board


def readBoard():
    n,m = map(int, input().split())
    board = []
    for x in range(n):
        board.append(input())
    return board


strs = readBoard()
printBoard(getSolve(strs))

 