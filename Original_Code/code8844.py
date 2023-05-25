import json
ch = []
data = {}
pd = json.loads(input())
for i in pd:
    data[i['name']] = i['parents']


def search(var):
    for key, value in data.items():
        if var in value:
            c.append(key)
            search(key)
    return len(set(c)) + 1


for i in data.keys():
    ch.append(i)
for i in sorted(ch):
    c = []
    print(i, "":"", search(i))
exit()
 