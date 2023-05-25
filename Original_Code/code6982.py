import sys
import math
from collections import defaultdict, deque

# поиск максимального потока в сети алгоритмом Форда-Фолкерсона
def ff_max_flow(input_lines):
    num_verts, num_edges = map(int, next(input_lines).split())
    start, end = 0, num_verts-1

    # преобразуем входные данные в массивы связности и массив ограничений
    adjacency, back_edges = defaultdict(set), defaultdict(set)
    capacity, flow = {}, {}
    start = end = 0
    for line in input_lines:
        a, b, cap = map(int, line.split())
        adjacency[a].add(b)
        back_edges[b].add(a)
        end = max(end, a, b)
        capacity[(a,b)] = cap
        flow[(a,b)] = 0

    def find_improveable_path():
        # путь Форда-Фалкерсона ищем поиском в ширину
        queue = deque([start])  # очередь следующего уровня поиска
        visited = set()         # множество уже пройденных вершин
        paths = {}              # здесь собираем найденные рёбра
        while queue:
            a = queue.popleft()
            if a in visited:
                continue
            visited.add(a)
            if a == end:  # нашли путь, если смогли дойти до конечной вершины
                return paths
            for b in adjacency[a]:
                # ищем прямые рёбра, в которые ещё можно добавить поток
                delta = capacity[(a,b)] - flow[(a,b)]
                if delta > 0:
                    if b not in paths:  # учитаываем только 1-й найденный (поиск в ширину)
                        paths[b] = (a, delta, 1)
                    queue.append(b)
            for b in back_edges[a]:
                # ищем обратные рёбра, из которых ещё можно убрать поток
                delta = flow[(b,a)]
                if delta > 0:
                    if a not in paths:  # учитаываем только 1-й найденный (поиск в ширину)
                        paths[a] = (b, delta, -1)
                    queue.append(b)
        return None  # путь не найден

    paths = find_improveable_path()
    while paths:
        # пройдём по пути в первый раз и найдём минимальную коррекцию
        delta_min = math.inf
        b = end
        while b != start:
            a, delta, sign = paths[b]
            delta_min = min(delta_min, delta)
            b = a

        # пройдём по пути во второй раз и скорректируем потоки
        b = end
        while b != start:
            a, delta, sign = paths[b]
            flow[(a,b)] += delta_min * sign
            b = a

        # продолжаем искать путь Форда-Фалкерсона, пока возможно
        paths = find_improveable_path()

    # наилучший поток равен сумме потоков в начале (или в конце)
    max_flow = sum(flow[(a,b)] for a,b in flow.keys() if a==start)
    return max_flow

#ff_max_flow(to_lines(test_input))
print(ff_max_flow(line for line in sys.stdin)) 