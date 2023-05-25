import numpy as np

V, E = input().split()
V, E = int(V), int(E)
M = np.zeros((V + 1, V + 1))
for i in range(E):
    from_, to_, weight = map(int, input().split())
    M[from_, to_]  = weight

start, end = input().split()
start, end = int(start), int(end)

known = set([start])
rest = set(range(1, V + 1))
rest.discard(start)
lengths = np.array([-1]*(V + 1))
lengths[start] = 0

last_vertex = start

while lengths[end] < 0 and end in rest:
    best_len = np.inf
    best_vertex = -1
    for possible_vertex in rest:
        for existed_vertex in known:
            if lengths[existed_vertex] < M[existed_vertex, possible_vertex]  + lengths[existed_vertex] < best_len:
                best_len = lengths[existed_vertex] + M[existed_vertex, possible_vertex]
                best_vertex = possible_vertex
    if best_vertex < 0: break
    known.add(best_vertex)
    rest.discard(best_vertex)
    lengths[best_vertex] = best_len
    
print(lengths[end])     