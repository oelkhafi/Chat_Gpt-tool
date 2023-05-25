import json
inp = json.loads(input().strip())# [{""name"": ""A"", ""parents"": []}, {""name"": ""B"", ""parents"": [""A"", ""C""]}, {""name"": ""C"", ""parents"": [""A""]}]
d, s = {}, {}
for i in inp:
    d[i['name']] = i['parents']
    s[i['name']] = 1
def search(lst, predok):
    for predok in d[predok]:
        lst.append(predok)
        search(lst, predok)
for exc in d:
    ttt = []
    for pr in d[exc]:
        search(ttt, pr)
    d[exc].extend(list(set(ttt)))
for i in d:
    if len(d[i]) >= 1:
        for p in set(d[i]):
            s[p] += 1
for x, y in sorted(s.items(), key=lambda x: x[0]):
    print(x,':',y) 