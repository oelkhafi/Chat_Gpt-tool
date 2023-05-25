def foo(c, p, d):
    global ans
    if c == p:
        ans = 'Yes'
        return
    if c in d:
        if p in dic[c]:
            ans = 'Yes'
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
for n in range(n):
    per, child = input().split()
    ans = 'No'
    foo(child, per, dic)
    print(ans)
 