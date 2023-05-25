namesp = {'global': None}
var = {'global':[]}

def create(ns, v):
  namesp[ns] = v
  var[ns] = []
  
def add(ns, v):
  var[ns].append(v)
  
def get(ns, v):
  if ns in var.keys():
    if v in var[ns]:
      print(ns)
    elif ns != 'global':
      return get(namesp[ns], v)
    else:
      print('None')
      
for i in range(int(input())):
  f, ns, v = input().split()
  if f == 'create':
    create(ns, v)
  elif f == 'add':
    add(ns, v)
  elif f == 'get':
    get(ns, v)




 