# put your python code here
s1,s2,d1,d2=[],[],{},{}
s1+=input()
s2+=input()
i,j=0,0
while i<len(s2):
    for x in s1:
        d1[x]=s2[i]
        i+=1
while j<len(s1):
    for x in s2:
        d2[x]=s1[j]
        j+=1
s3,s4=[],[]
s3+=input()
s4+=input()
for x in s3:
    print(d1[x],end='')
print()
for x in s4:
    print(d2[x],end='') 