a={'+', ' ', '-', '(', ')'}
d={}
for i in iter(input,'.'):
    if len(i.split())==1:
        if d.get(i.split()[0])!=None:
            print(*d.get(i.split()[0]), sep=', ')  
        else:
            print(""Не найдено"")
    if len(i.split())>1:
        number=i.split(maxsplit=1)[1].split(', ')
        for p in number:
            p=''.join([j for j in p if j not in a])
            if len(p)==11:
                if p[0]=='7' or p[0]=='8':
                    p='+7 ('+ p[1:4]+') '+p[4:7]+'-'+p[7:9]+'-'+p[9:11]
                    d[i.split()[0]]=d.setdefault(i.split()[0],[])+[p]




 