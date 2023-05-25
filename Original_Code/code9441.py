n=int(input())
s=[]
for i in range(n):
    s+=[str(input()).split()]
s1={'None':[],'global':[]}
s2={'None':['global']}
var=''
namespace=''
for i in range(len(s)):
    if s[i][0]=='add':
        s1[s[i][1]]=[]
    elif s[i][0]=='create':
        s2[s[i][2]]=[]
        s1[s[i][1]]=[]
for i in range(len(s)):
    if s[i][0]=='add':
        s1[s[i][1]]+=[s[i][2]]
    elif s[i][0]=='create':
        s2[s[i][2]]+=[s[i][1]]
def searchvar(namespace,var):
    if var in s1[namespace]:
        return namespace
    else:
        for key in s2:
            if namespace in s2[key]:
                namespace=key
                return searchvar(namespace,var)
for i in range(len(s)):
    if s[i][0]=='get'and s[i][1] not in list(s2.keys()) and s[i][1] not in list(s1.keys()):
        print(None)
        continue
    elif n==1:
        print(None)
        break
    elif s[i][0]=='get':
        var=s[i][2]
        namespace=s[i][1]
        print(searchvar(namespace,var))




 