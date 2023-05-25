namespase_classes={}

def abc(val_1):
    for j in namespase_classes.get(val_1):
        c.append(j)
        if j not in namespase_classes:
            pass
        else:
            abc(j)
    return c

for i in range(int(input())):
    a=input().replace(' : ',' ').split()                #'D : B C' -> 'D B C' -> ['D','B','C']
    if len(a)==1:
        namespase_classes[a[0]] = []
    elif len(a)>1:
        namespase_classes[a[0]] = a[1:]


b=[]
for k in range(int(input())):
    cnt = 0
    c=[]
    x = input()
    if x in b:
        print(x)
    else:
        for m in abc(x):
            if m in b:
                cnt+=1
        if cnt>0:
            print(x)
        else:
            b.append(x)
 