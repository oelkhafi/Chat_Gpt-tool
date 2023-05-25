a=int(input())
b=int(input())
c=int(input())
d=int(input())
cd=''
ab=''
e=0
for i in range(c, d + 1):
    cd = cd + '\t' + str(i)
print(cd)
for j in range (a,b+1):
    if j==b+1:
        print('\n')

    for i in range(c, d + 1):
        if i==c:
            ab = ab + str(j) + '\t' + str(i * j) + '\t'
        else:
            ab = ab  + str(i * j) + '\t'
        if i==d:
            print(ab,end='\n')
            ab=''


print(ab)
 