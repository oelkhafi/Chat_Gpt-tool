n=int(input())
s=0
slg=[]
if n<=2:
    print(1)
    print(n)
else:
    for i in range(1,n):
        s+=i
        if s<=n:
            slg.append(i)
        elif s>n:
            slg[i-2]=slg[i-2]+(n-(s-i))
            break
print(len(slg))
for sl in slg:
    print(sl, end="" "")




 