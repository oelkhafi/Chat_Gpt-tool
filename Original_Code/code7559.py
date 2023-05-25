import requests

import re

file = input().strip()
resp = requests.get(file).text
pattern = r'<a.*href=[\'\""](?:.*?:\/\/)?([^\.][\w.-]*)\/?.*[\'\""].*>'
url = re.findall(pattern, resp)
m = set()
res = []

for i in url:
    m.add(i)
    
for i in m:
    res.append(i)
    
res.sort()

for i in res:
    print(i)
     