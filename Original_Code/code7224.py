def code(x, y):
    for i in x:
        bit[i] = y + bit.get(i, '')

s = input()
tmp, bit, res = [], {}, ''
for i in set(s):
    tmp.append((s.count(i), i))
n = k = len(tmp)
if n == 1:
    bit[tmp[0][1]] = '0'
else:
    while k > 1:
        a = tmp.pop(tmp.index(min(tmp)))
        code(a[1], '0')
        b = tmp.pop(tmp.index(min(tmp)))
        code(b[1], '1')
        tmp.append((a[0] + b[0], a[1] + b[1]))
        k -= 1
for i in s:
    res += bit[i]
print(n, len(res))
for i in sorted(set(s)):
    print(i + ': ' + bit[i])
print(res) 