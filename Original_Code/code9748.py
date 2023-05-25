errors_space = {}
errors_list = []
dont_err = []

def check_er(graph, start):
    parents = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in parents:
            parents.add(vertex)
            if vertex in graph:
                stack.extend(graph[vertex] - parents)
    return parents

for i in range(int(input())):
    tmp_lst = input().split(' : ')
    if len(tmp_lst) > 1:
        errors_space[tmp_lst[0]] = set(tmp_lst[1].split(' '))

for i in range(int(input())):
    err = input()
    if check_er(errors_space, err).intersection(set(errors_list)):
        dont_err.append(err)
    errors_list.append(err)

print(*dont_err, sep='\n')
 