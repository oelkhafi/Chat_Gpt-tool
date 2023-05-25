b=[]
a= input().split(', ')
for i in range(len(a)):
    b.append(int(a[i]))
b1=sorted(b)
if b1[len(b1)-2]>=abs(b1[0]) and b1[len(b1)-2]>=abs(b1[1]):
    if abs(b1[len(b1)-2])>=abs(b1[len(b1)-1]):
        print(b1[len(b1)-1],b1[len(b1)-2])
    else:
        print(b1[len(b1)-2],b1[len(b1)-1])
elif abs(b1[0])>=abs(b1[1]) and abs(b1[1])>abs(b1[len(b1)-1]):
    if abs(b1[0])>=abs(b1[1]):
        print(b1[1], b1[0])
    else:
        print(b1[0], b1[1])
else :
    if abs(b1[len(b1)-1])>=abs(b1[0]):
        print(b1[0],b1[len(b1)-1])
    else:
        print(b1[len(b1)-1],b1[0])




 