import sys


def nd(node, r=''):
    for i in range(len(node)):
        if isinstance(node[i], list):
            nd(node[i], r + str(i))
        else:
            h2.append((node[i], r + str(i)))
    return

s = sys.stdin.readline().strip('\n')
lts = set(s)
h = [[s.count(lt), lt] for lt in lts]

while len(h) > 2:
    p0 = h.pop(h.index(min(h, key=lambda x: x[0])))
    p1 = h.pop(h.index(min(h, key=lambda x: x[0])))
    h.append([p0[0] + p1[0], [p0[1], p1[1]]])
h = [now[1] for now in h]

h2 = []
nd(h)
h2.sort()
h_dict = dict(h2)
s_out = ''
for now in s:
    s_out += h_dict[now]

sys.stdout.write(f'{len(lts)} {len(s_out)}\n')
for now in h2:
    sys.stdout.write(f'{now[0]}: {now[1]}\n')
sys.stdout.write(s_out)
 