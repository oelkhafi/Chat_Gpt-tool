def vSum(a,b):
    return (a[0]+b[0], a[1]+b[1])

def canWalk(matrix, direction):
    n = len(matrix)
    return 0<=direction[0]<n and 0<=direction[1]<n and matrix[direction[0]][direction[1]] is None

def rotateClockwise(d):
    if d[1]:
        return d[1],0
    else:
        return 0, -d[0]
    
n = int(input())
matrix = [[None]*n for _ in range(n)]

position = (0,0)
cur_value = 1
rotations = 0
matrix[position[0]][position[1]] = cur_value
direction = (0,1)
while rotations<2:
    new_pos = vSum(position,direction)
    if canWalk(matrix, new_pos):
        rotations = 0
        cur_value+=1
        position = new_pos
        matrix[new_pos[0]][new_pos[1]] = cur_value
    else:
        rotations+=1
        direction = rotateClockwise(direction)
        
for row in matrix:
    print(*row) 