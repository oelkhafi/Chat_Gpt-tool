d={}
name={}
for i in input().split(','):
       d[i.split('""')[-1][1:]]=d.setdefault(i.split('""')[-1][1:],[])+[''.join(i.split('""')[1:-1])]
for i in iter(input, '.'):
            if i.split()[0]!='Посоветуй':
                name[i.split()[0]]=name.setdefault(i.split()[0],set())|{' '.join(i.split()[1:])[1:-1]}
            else:
                give=i.split()[-1][1:-1]
                name[give]=name.setdefault(give,set())
                s={}
                for j in name[give]:
                    for k in d:
                        if j in d[k]:
                            s[k] = s.get(k, 0) + 1
                k=[]
                for l,v in s.items():
                    if v==max(s.values()):
                        k+=['""'+d[l][i]+'""' for i in range(len(d[l])) if d[l][i] not in name[give]]
                if len(k)>0:
                    print(*k, sep="", "")  
                else: 
                    print ('Список пуст')
                     
                     


 