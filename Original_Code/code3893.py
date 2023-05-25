from collections import defaultdict


def get_parents(exs):
    child2parents = defaultdict(list)
    for ex in exs:
        if len(ex) == 2:
            child2parents[ex[0]] += ex[1].split()
    return child2parents


def get_excluded(exs, n_exs):
    
    def _exclude(parents, _ex):
        if parents:
            for a in parents:
                if a in caught:
                    if _ex not in excluded:
                        excluded.append(_ex)
                _exclude(child2parents.get(a, None), _ex)

    caught = set()
    excluded = []
    child2parents = get_parents(exs)

    for _ in range(n_exs):
        ex = input()
        _exclude(child2parents.get(ex, None), ex)
        caught.add(ex)
    return excluded


n_classes = int(input())
exceptions = [[l.strip() for l in input().split("":"")] for _ in range(n_classes)]
n_caught = int(input())
print(*get_excluded(exceptions, n_caught), sep='\n')

 