namespaces = {'global': None}
varibles = {'global': set()}
def create(nmsp, prnt):
    namespaces[nmsp] = prnt
    varibles[nmsp] = set()

def add(nmsp, var):
    varibles[nmsp].add(var)

def get(nmsp, var):
   if nmsp == None:
       print(nmsp)
   elif var in varibles[nmsp]:
       print(nmsp)
   else:
       get(namespaces[nmsp], var)


for i in range(int(input())):
    cmd, nmsp, var = input().split()
    if cmd == 'create':
        create(nmsp, var)
    elif cmd == 'add':
        add(nmsp, var)
    else:
        get(nmsp, var)





 