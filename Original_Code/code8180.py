import sys 

lines = sys.stdin.readlines()
v_num, e_num = map(int, lines[0].split())
a_list = [[] for _ in range(v_num)]
for line in lines[1:]:
    v1, v2 = map(int, line.split())
    a_list[v1 - 1].append(v2 - 1)
    a_list[v2 - 1].append(v1 - 1)

visited = [False] * v_num


def dfp(v):
    visited[v] = True
    for n in a_list[v]:
        if not visited[n]:
            dfp(n)

components = 0

for v in range(v_num):
    if not visited[v]:
        components += 1
        dfp(v)

print(components)
 