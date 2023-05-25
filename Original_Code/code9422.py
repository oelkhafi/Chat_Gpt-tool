s=input()
i=0
j=1
b=len(s)
a=s[i]
if b>1:
    c=s[i+1]
    d=0
    for d in range(1,1000):
        while a==c:
            j+=1
            i+=1
            a=s[i]
            if i<b-1:
                c=s[i+1]
            else:
                print(a,end='')
                print(j,end='')
                break
        while a!=c:
            print(a,end='')
            print(j,end='')
            j=1
            i+=1
            a=s[i]
            if i<b-1:
                c=s[i+1]
            else:
                print(a,end='')
                print(j,end='')
                break
        if i==b-1:
            break
else:
    print(a,end='')
    print(1,end='')




 