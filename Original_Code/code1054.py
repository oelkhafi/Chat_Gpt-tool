s=0
a0=int(input())
a=input().split()
a=sorted(a)
a.reverse()
for i in range(0, len(a)-1):
    if int(a[i])>=a0>int(a[i+1]) and a.count(a[i])==1 :
        s=i+2
    elif int(a[i])>=a0>int(a[i+1]) and a.count(a[i])>1  :
         s=i+a.count(a[i])
    elif a0>int(a[0]) and a.count(a[0])==1:
        s=1
    elif a0==int(a[0]) and a.count(a[0])>1:
        s=1+a.count(a[0])
    elif a0==int(a[len(a)-1]) and a.count(a[len(a)-1])==1:
        s=len(a)+1
    elif a0<int(a[len(a)-1]):
        s=len(a)+1
print (s)



 