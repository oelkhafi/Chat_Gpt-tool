d = dict()
for i in range(int(input())):
    v = input().replace(':','')
    v = v.strip()
    v = v.split()
    d.update({v[0]: list(v[1:])})
for i in range(int(input())):
    v = input().split()
    if len(v) == 1 and v[0] in d: print('Yes'); continue
    def search(F, S):
        FFF = False
        if not S in d: return False 
        if F in d[S] or F == S:
            return True
        else:
            for pr in d[S]:
                if (len(d[pr])!=0): FFF = search(F, pr) 
                if FFF: break
        return FFF
    if search(*v):
        print('Yes')
    else:
        print('No') 