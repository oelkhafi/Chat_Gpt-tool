abcin=str(input())
abcout=str(input())
toshif=str(input())
todeshif=str(input())
shif=[]
deshif=[]
for i in toshif:
    for k in range(len(abcin)):
        if i==abcin[k]:
            shif.append(abcout[k])
for z in todeshif:
    for o in range(len(abcout)):
        if z==abcout[o]:
            deshif.append(abcin[o])
for x in shif:
    print(x,end='')
print()
for r in deshif:
    print(r,end='')




 