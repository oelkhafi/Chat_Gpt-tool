# put your python code here
import json

def getChilds(parent):
    if parent not in d or len(d[parent]) == 0:
        return [parent]
    else:
        l = [parent];
        for child in d[parent]:
            l.extend(getChilds(child))
        return l

data = json.loads(input())
d = {}
for row in data:
    for i in row['parents']:
        if i in d:
            d[i].append(row['name'])
        else:
            d[i] = [row['name']]
    if row['name'] not in d:
        d[row['name']] = []
for key in sorted(d.keys()):
    print(key, len(set(getChilds(key))), sep=' : ')



 