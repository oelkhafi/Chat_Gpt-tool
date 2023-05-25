from collections import Counter

to_code = input()
c = Counter(to_code)
freq = [(su, sym) for sym, su in c.items()]
freq.sort(reverse=True)
d = dict()
if len(freq) == 1:
    d[freq[0][1]] = '0'
else:
    while len(freq) >= 2:
        node1, node2 = freq.pop(), freq.pop()
        for sym in node1[1]:
            d[sym] = '0' + d.get(sym, '')
        for sym in node2[1]:
            d[sym] = '1' + d.get(sym, '')
        sym_new = node1[1] + node2[1]
        freq_new = node1[0] + node2[0]
        freq.append((freq_new, sym_new))
        freq.sort(reverse=True)
        # print(freq, '\n', d, '\n')

total_code_len = sum([len(d[sym])*count for sym, count in c.items()])

print(len(c), total_code_len)

codes = sorted(d.items(), key= lambda x: len(x[1]))
print(*[f'{sym}: {code}' for sym, code in codes], sep='\n')

print(*[d[sym] for sym in to_code], sep='')
 