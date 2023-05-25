def foo(c, p, d):
    global ans
    if c == p:
        ans = True
        return
    if c in d:
        if p in dic[c]:
            ans = True
        else:
            temp = dic[c]
            for val in temp:
                foo(val, p, temp)


n = int(input())
dic = {}
for n in range(n):
    lst = input().split(' : ')
    dic[lst[0]] = [] if len(lst) == 1 else lst[1].split()
n = int(input())
err = []
for n in range(n):
    err += [input()]
s = set()
for j, val in enumerate(err):
    for i in range(j + 1, len(err)):
        ans = False
        foo(err[i], val, dic)
        if ans is True:
            if err[i] not in s:
                s.add(err[i])
for val in err:
    if val in s:
        print(val)
 