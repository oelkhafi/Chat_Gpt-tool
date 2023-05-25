# put your python code here
import json
from collections import Counter
z = []
d = dict()
s = set()
m = dict()

def countClass(classParent):
    if d[classParent] != []:
        for i in d[classParent]:
            countClass(i) 
            m[k].add(i)

data = json.loads(input())
for className in data:
    d[className['name']] = className['parents']
for k in d.keys():
    m[k] = set()
    if d[k] != []:
        for classname in d[k]:
            m[k].add(classname)
            countClass(classname)
for key in m.keys():
    z.append(key)
    for t in m[key]:
        z.append(t)
c = Counter(z)
for k in sorted(c.keys()):
    print (k, ':', c[k]) 