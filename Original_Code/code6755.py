import json

output = dict()
py_obj = json.loads(input())

def checker(key,  dict):
    for i in dict[key]:
        for j in dict[i]:
            checker(j, dict)
            if j not in dict[key]:
                dict[key].append(j)

for i in py_obj:
    output[i['name']] = []
for i in py_obj:
    for l in i['parents']:
        if i['name'] not in output[l]:
            output[l].append(i['name'])
for key in output.keys():
    checker(key, output)

for key in sorted(output.keys()):
    print(key + ' : ' + str(len(output[key]) + 1))

 