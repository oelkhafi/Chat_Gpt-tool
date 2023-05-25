import requests       
import re

links_list = []
link = input().strip()
r = requests.get(str(link))
links_list.extend(re.findall(r'<a.*>', r.text))
b = []
for i in links_list:
    b += re.findall(r'<a.*?//([\w.-]+)[/>]?', i)
for i in links_list:
    t = re.findall(r'<a\s?href\s?=\s?[\'\""]([\w.-]*)[\'\""]>', i)
    if t not in b:
        b += t

b = set(b)
b = list(b)
print(*sorted(b), sep='\n')





 