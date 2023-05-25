scopes = {'global': {'parent': None, 'variables': set()}}

def create(namespace, parent):
  scopes[namespace] = {'parent': parent, 'variables': set()}

def add(namespace, var):
  scope_to_add = scopes[namespace]
  scope_to_add['variables'].add(var)

def get(namespace, var):
  scope_to_get = scopes[namespace]
  if var in scope_to_get['variables']:
    return print(namespace)
  elif scope_to_get['parent'] != None:
    get(scope_to_get['parent'], var)
  else:
    return print(None)    


for i in range(int(input())):
  cmd, nsp, arg = input().split()
  if cmd == 'create':
    create(nsp, arg)
  elif cmd == 'add':
    add(nsp, arg)
  elif cmd == 'get':
    get(nsp, arg)
 