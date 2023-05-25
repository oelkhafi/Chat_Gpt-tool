tree = dict()


def find(par, cl, path=0):
    if par == cl and cl in tree:
        return 1

    elif not tree.get(cl) or not tree[cl]:
        return 0

    elif par in tree[cl]:
        return 1

    else:
        for value in tree[cl]:
            path += find(par, value)

    return path


n = int(input())

for cl in range(n):
    cl = input().split()

    if cl[0] not in tree:
        tree[cl[0]] = []

    if len(cl) > 1:
        for j in range(2, len(cl)):
            tree[cl[0]].append(cl[j])

            if cl[j] not in tree:
                tree[cl[j]] = []

#print(tree)

m = int(input())
step = []

for exc in range(m):
    exc = input()
    i = 1

    for s in step:
        if find(s, exc):
            i = 0
            break

    if i != 0:
        step.append(exc)
    else:
        print(exc)

 