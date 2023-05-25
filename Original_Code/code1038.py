s=[]
while True:
    a=input()
    if a=='.':
        s.sort()
        if len(s)%2==0:
            r=len(s)//2
            print(round(s[r]+s[r-1])/2)
            break
        else:
            r=len(s)//2
            print(s[r])
            break            
    elif True:
        s.append(int(a))     
 




 