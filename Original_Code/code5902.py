def mx(d):
    d=str(abs(d))
    a=[int(i) for i in d]
    b=len(a)
    c=''
    for i in range (b):
        c+=str(max(a))
        a.pop(a.index(max(a)))
    l=int(c)
    return l
n=int (input())
k=[int(input()) for i in range(n)]
nol=0
for i in k:
    if mx(i)>nol:
        nol=mx(i)
        cet=i
print(cet)




 