import json
# import sys
# sys.stdin = open(""input.txt"", ""r"")


def foo(x):
    k = set(kids[x])
    for ii in kids[x]:
        k.update(foo(ii))
    return k


s = json.loads(input())
kids = {}
for i in s:
    kids.setdefault(i['name'], [])
    for j in i['parents']:
        if kids.get(j) is None:
            kids[j] = [i['name']]
        else:
            kids[j].append(i['name'])

keys = sorted(list(kids.keys()))
for i in keys:
    print(f'{i} : {len(foo(i))+1}')
 