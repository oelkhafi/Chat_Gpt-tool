def foo(sym):
    tmp = ''
    for i in d2.items():
        if len(i[1]) > 0:
            if sym in i[1][1]:
                tmp = '0' + tmp
            elif sym in i[1][0]:
                tmp = '1' + tmp
        code[sym] = tmp   

stin, stout = input(), ''
d1, d2, d3, code = list(), dict(), list(), dict()

for i in stin:
    if ([i, stin.count(i)]) not in d1:
        d1.append([i, stin.count(i)])
        d2[i] = []
        d3.append(i)
while len(d1) > 1:
    d1 = list(sorted(d1, key=lambda x: x[1], reverse=True))
    t1, t2 = d1.pop(), d1.pop()
    d2[t1[0]+t2[0]] = [t1[0], t2[0]]
    d1.append([t1[0]+t2[0], t1[1]+t2[1]])
for i in d3:
    foo(i)
for i in stin:
    stout += code[i]
if len(d2) == 1:
    print(len(d2), d1[0][1])
    print(d1[0][0] + ':', '0')
    print(int(d1[0][1])*'0')
else:
    print(len(code), len(stout))
    for i in code.items():
        print(i[0] + ':', i[1])
    print(stout)
 