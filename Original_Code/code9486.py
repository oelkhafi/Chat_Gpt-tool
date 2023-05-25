import re
import requests

def getref(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return [match.group() for match in re.finditer(r'(https?|ftp):\/\/[^\s\/$.?#].[^\s>""]*', resp.text)]
    else:
        return []
    
urlA, urlB = [input() for _ in range(2)]

urlist = getref(urlA)

res = 'No'
for url in urlist:
    if urlB in getref(url):
        res = 'Yes'
        break
print(res)
 