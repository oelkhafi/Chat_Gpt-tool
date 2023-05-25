x=int(input())
cl={}
for i in range(x):
    st=input().split()
    if len(st)==1:
        cl[st[0]]=[]
    else:
        for k in range(2, len(st)):
            if st[0] not in cl:
                cl[st[0]]=[st[k]]
            else:
                cl[st[0]].append(st[k])
for i in cl:
    for j in cl[i]:
        if j in cl:
            cl[i]+=cl[j]
x=int(input())
st=[]
st1=[]
for i in range(x):
    st.append(input())
for j in range(len(st)):
    for i in range(len(st)):
        if (st[i] in cl[st[j]]) and (i<j):
            if st[j] not in st1:
                st1.append(st[j])
for i in st1:
    print(i)

 