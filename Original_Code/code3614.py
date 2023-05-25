dict = {}
for i in range(int(input())):
    s = input()
    if s.split()[0] not in dict:
        if len(s.split()) == 1: 
            dict[s] = []
        else:
            dict[s.split()[0]] = s.split()[2:]
    else:
        dict[s.split()[0]] += s.split()[2:]
        
def rec(l, r):
    try:
        if l in dict[r]:
            return 'Yes'
        elif l == r:
            return 'Yes'
        else:
            if len(dict[r]) == 1:
                return rec(l, dict[r][0])
            elif len(dict[r]) > 1:
                for i in range(len(dict[r])):
                    if rec(l, dict[r][i]) == 'Yes':
                        return 'Yes'
        return 'No'
    except:
        return 'No'
    
for i in range(int(input())): 
    L = input().split(' ')
    if len(L) > 1:
        print(rec(L[0], L[1]))
    else:
        print('Yes') 