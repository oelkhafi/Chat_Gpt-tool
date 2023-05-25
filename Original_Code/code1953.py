d = {}
addErr = set()
nope = []

def check(el, origin):
  if (el not in addErr and d[el] == None):
    pass
  else:
    for node in d[el]:
      if (node in addErr):
        if (origin not in nope):
          nope.append(origin)
      elif (node not in addErr and d[node] != None):
        check(node, origin)

for points in [input().split(':') for i in range(int(input()))]:
  if(len(points) > 1):
    d[points[0].replace(' ', '')] = tuple(points[1].split())
  else:
    d[points[0].replace(' ', '')] = (None)

for points in [input().replace(' ', '') for i in range(int(input()))]:
  check(points, points)
  addErr.add(points)

for x in nope:
  print(x) 