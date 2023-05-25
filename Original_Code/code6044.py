import json

x = {}
def inp(d):
    n, p = d[0][1], d[1][1]
    for i in p:
        x[i] = [n] if i not in x else x[i]+[n]
    if n not in x: 
        x[n] = []

def ans(k):
    for j in x[k]:
        s.add(j)
        ans(j)

json.loads(input(), object_pairs_hook=inp)

for k in sorted(x):
    s = set()
    ans(k)
    print(k, ':', (len(s)+1)) 