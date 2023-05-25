# put your python code here
import requests, re

links, secondLinks = [], []

a = re.findall(r'\<a\s.+?>.*?\<\/a>', requests.get(input()).text)
b = input()
for i in a:
    if re.search(r'http[s]*:', i):
        res = re.findall(r'href=[\""\'](.+?)[\""\']', i)    
        links.append(res[0])
for link in links:
    x = requests.get(link)
    if x.status_code == 200:
        x = re.findall(r'\<a\s.+?>.*?\<\/a>', requests.get(link).text)
        for n in x:
            if re.search(r'http[s]*:', n):
                res = re.findall(r'href=[\""\'](.+?)[\""\']', n)    
                secondLinks.append(res[0])
        
if b in secondLinks:
    print('Yes')
else:
    print('No')
 