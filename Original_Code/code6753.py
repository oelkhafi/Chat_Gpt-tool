import requests
import re

pattern = r'.*\""(.*?)\"".*'
link1 = input()
link2 = input()
res = requests.get(link1)
status = ''
if res.status_code == 200:
    for link in re.findall(pattern, res.text.rstrip()):
        res1 = requests.get(link)
        for url in re.findall(pattern, res1.text.rstrip()):
            if url == link2:
                status = True
                break

else:
    status = False
if status:
    print('Yes')
else:
    print('No')




 