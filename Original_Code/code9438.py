d=int(input())
s1=set()
s2=set()
s3=set()
for i in range(d):
    s=str(input()).lower()
    s1.add(s)
l=int(input())
for j in range(l):
    a=str(input()).lower().split(' ')
    b=len(a)
    for k in range(b):
        s2.add(a[k])
for key in s2:
    if key not in s1:
        s3.add(key)
for x in s3:
    print(x)




 