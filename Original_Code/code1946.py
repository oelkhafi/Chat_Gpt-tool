d = dict()
d['global'] = {'parent': 'None'}
def creating(nmsp, var):
  d[nmsp] = {'parent': (var)}

def adding(nmsp, var):
  if (nmsp in d):
    if ('var' in d[nmsp]):
      d[nmsp]['var'] += [var]
    else:
      d[nmsp].update({'var': [var]})

def reception(nmsp, var):
  if (d[nmsp].get('parent', ()) == 'None' and var not in d[nmsp].get('var', [])):
    print(d[nmsp].get('parent', ()))
  elif (var in d[nmsp].get('var', [])):
    print(nmsp)
  else:
    return reception(d[nmsp].get('parent', ()), var)

def actionSelection(cmd, nmsp, var):
  if (cmd == 'create'):
    creating(nmsp, var)
  elif (cmd == 'add'):
    adding(nmsp, var)
  else:
    reception(nmsp, var)

for i in range(int(input())):
  cmd, nmsp, var = input().split()
  actionSelection(cmd, nmsp, var) 