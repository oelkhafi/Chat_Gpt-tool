F = {}


def walk(node, s=''):
    if not node[2]:
        F[node[0]] = s or '0'
    else:
        walk(node[2][0], s + '1')
        walk(node[2][1], s + '0')


s = input()
s_set = set(s)
H = sorted([(i, s.count(i), []) for i in s_set],
           key=lambda x: x[1],
           reverse=1)
while len(H) > 1:
    a = H.pop()
    b = H.pop()
    H.append((None, a[1] + b[1], [a, b]))
    H = sorted(H,
               key=lambda x: x[1],
               reverse=1)

walk(H[0])
s = ''.join(F[i] for i in s)
print(len(s_set), len(s))
for i in sorted(F.items()):
    print('{}: {}'.format(i[0], i[1]))
print(s)
 