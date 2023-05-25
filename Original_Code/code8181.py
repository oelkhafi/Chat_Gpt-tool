import sys

lines = sys.stdin.readlines()
v_num, e_num = map(int, lines[0].split())

aj_list = [[] for _ in range(v_num)]
for line in lines[1:]:
    v1, v2 = map(int, line.split())
    aj_list[v1].append(v2)
    aj_list[v2].append(v1)

distances = v_num * [None]

added_in_q = v_num * [False]
added_in_q[0] = True
queue = [(0, 0)]
while len(queue):
    v, length = queue.pop()
    distances[v] = length
    for child in aj_list[v]:
        if not added_in_q[child]:
            added_in_q[child] = True
            queue.insert(0, (child, length + 1))

print(*distances) 