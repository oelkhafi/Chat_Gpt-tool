def add(spisok):
    if spisok[0] in ns.keys():
        ns[spisok[0]]['vars'].extend(spisok[2:len(spisok)])
    else:
        ns[spisok[0]] = {'vars': []}
        ns[spisok[0]]['vars'].extend(spisok[2:len(spisok)])


def get(m_parent, child):
    if child in m_parent[:-1]:
        return child
    else:
        for i in ns[child]['vars']:
            midl_res = get(m_parent, i)
            if midl_res == i:
                return child


ns = dict()
for j in range(int(input())):
    spisok = []
    spisok.extend([i for i in (input().split())])
    if len(spisok) == 1:
        ns[spisok[0]] = {'vars': []}
    else:
        add(spisok)


result = []
temp_in = []
for k in range(int(input())):
    a = input()
    temp_in.append(a)
    result.append(get(temp_in, a))

for i in range(len(result)):
    if result[i] is not None: print(result[i]) 