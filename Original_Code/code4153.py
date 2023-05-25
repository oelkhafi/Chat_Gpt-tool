def add(spisok):
    if spisok[0] in ns.keys():
        ns[spisok[0]]['vars'].extend(spisok[2:len(spisok)])
    else:
        ns[spisok[0]] = {'vars': []}
        ns[spisok[0]]['vars'].extend(spisok[2:len(spisok)])


def get(m_parent, child):
    if child not in ns.keys():
        return 'No'
    if m_parent in ns[child]['vars'] or m_parent == child:
        return 'Yes'
    elif len(ns[child]['vars']) == 0:
        return 'No'
    else:
        for i in ns[child]['vars']:
            midl_res = get(m_parent, i)
            if midl_res == 'Yes':
                return midl_res
        return 'No'


ns = dict()
for j in range(int(input())):
    spisok=[]
    spisok.extend([i for i in (input().split())])
    if len(spisok) == 1:
        ns[spisok[0]] = {'vars': []}
    else:
        add(spisok)
        

result = []
for k in range(int(input())):
    m_parent, child = input().split()
    result.append(get(m_parent, child))
        
for i in range(len(result)):
    print(result[i])
 