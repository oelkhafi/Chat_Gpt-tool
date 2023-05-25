import json

def parents(name, data):
    for r in data:
        if r[""name""] == name:
            return r[""parents""]
    return []

def walk(from_, to_, data):
    for p in parents(from_, data):
        if p == to_:
            return True
        else:
            part = walk(p, to_, data)
            if part:
                return part
    return False

ans = {}
js = json.loads(input())
for i in js:
    for j in js:
        a = i['name']
        b = j['name']
        if b not in ans:
            ans[b] = 1
        if a != b and walk(a, b, js):
            ans[b] += 1
for k, v in dict(sorted(ans.items())).items():
    print(k, ':', v) 