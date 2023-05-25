def bit(a, b=''):
    if isinstance(a[0], str):
        c[a[0]] = b + '0'
    else:
        bit(a[0], b+'0')
    if isinstance(a[1], str):
        c[a[1]] = b + '1'
    else:
        bit(a[1], b+'1')


s, d, c = input(), {}, {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
n = len(d)
if n > 1:
    while len(d) > 1:
        k1 = min(d.keys(), key=d.get)
        v1 = d.pop(k1)
        k2 = min(d.keys(), key=d.get)
        v2 = d.pop(k2)
        d.update({(k1, k2): v1+v2})
    bit(d.popitem()[0])
else:
    c[s[0]] = '0'
b = ''.join(c[i] for i in s)
print(str(n)+' '+str(len(b))+'\n'+'\n'.join(i+': '+c[i] for i in c)+'\n'+b)
 