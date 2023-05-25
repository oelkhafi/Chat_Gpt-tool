d = {}

for i in range(int(input())):
    t = input().split(' : ')
    if len(t) == 1:
        t.append('')
    d[t[0]] = t[1].split()
    for j in d[t[0]]:
        if j not in d:
            d[j] = []


def is_parent(child, parent):
    if parent in d[child] or child == parent:
        return True
    if len(d[child]):
        return any(map(lambda x: is_parent(x, parent), d[child]))


for i in range(int(input())):
    s = input().split()
    print('Yes' if is_parent(s[1], s[0]) else 'No')
 