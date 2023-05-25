import json

def foo(c, p, d):
    global ans
    if c == p:
        ans = True
        return
    if c in d:
        if p in cls[c]:
            ans = True
        else:
            temp = cls[c]
            for val in temp:
                foo(val, p, temp)

data = json.loads(input())
cls = {}
res = {}
for dic in data:
    cls[dic['name']] = dic['parents']
    res[dic['name']] = 0

for cls_per in res:
    for cls_ch in res:
        ans = False
        foo(cls_ch, cls_per, cls)
        if ans:
            res[cls_per] += 1

res_sort = list(res.keys())
res_sort.sort()
for i in res_sort:
    print(i, ':', res[i])
 