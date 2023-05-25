def creates(func,parrent):
    queries.append([func,parrent])
def adds (func,var):
    for step in range (len(queries)):
        if queries[step][0] == func:
            queries[step].append(var)
            return
def gets (func,var):
    for step in range (len(queries)):
        if queries[step][0] == func:
            if var in queries[step]:
                return queries[step][0]
            elif queries[step][1]==""None"":
                return None
            else:
                return gets(queries[step][1], var)
def parse(x,y,z):
    if x == ""create"" :
        creates(y,z)
    elif x == ""add"" :
        adds(y,z)
    elif x == ""get"" :
        quer.append(gets(y,z))
queries =[[""global"",""None""]]
quer=[]
enter=int (input())
for i in range (enter):
    x,y,z=input().split()
    parse(x,y,z)
for i in quer:
    print(i) 