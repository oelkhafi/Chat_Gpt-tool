w = input()
b = ['(','{','['] 
e = [')','}',']']
s = []
isSuccess = True
for i in range(len(w)):
    if w[i] in b:
        s.append((w[i],i))
    if w[i] in e:
        index = e.index(w[i])
        if len(s)==0 or s.pop()[0]!=b[index]:
            isSuccess = False
            break
        
if isSuccess:
    if len(s)==0:
        print('Success')
    else:
        print(s[0][1]+1)
else:
    print(i+1)



 