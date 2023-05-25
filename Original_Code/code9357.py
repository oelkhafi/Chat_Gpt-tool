# put your python code here
def getspace(namesp,var):
    if var in dic[namesp]:
        return(namesp)
    if namesp=='global' and var not in dic.get(namesp):
        return('None')
    else:
        return(getspace(dic_prnt[namesp],var))
        
    
    
dic={'global':[]}
dic_prnt={'global': 'None'}
for i in range(int(input())):
    cmd, namesp, var =input().split()
    if cmd=='create':
        dic[namesp]=[]
        
        dic_prnt[namesp]=var
    elif cmd=='add':
        dic[namesp].append(var)
    elif cmd=='get':
        print(getspace(namesp,var))

    



 