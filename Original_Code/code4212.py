# put your python code here
import requests
import re

a, b = input(), input()
found = False
res = requests.get(a)
if res.status_code != 200:
    print('No')
else:
    links = re.findall(r'<a href=\""(.*)\"">',res.text)
    for link in links:
        res = requests.get(link)
        if res.status_code == 200 and b in res.text:
            found = True
            break
    if found:
        print('Yes')
    else:
        print('No')


 