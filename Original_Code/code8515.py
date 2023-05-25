# put your python code here
a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=a
print(' ',end='\t')
for k in range(c,d+1):
    print(k,end='\t')
print('')
while f<=b:
    for i in range(a,b+1):
        print(f,end='\t')
        for j in range(c,d+1):
            print(i*j, end='\t')
        print('')
        f +=1



 