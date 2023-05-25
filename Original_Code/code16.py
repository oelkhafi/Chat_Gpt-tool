import requests as req
import re
a=input()
b=input()
o=False
res=req.get(a)
if res.status_code==200:
    s=re.findall(r""href=\""(.+)\"""",res.text)
    for i in s:
        res=req.get(i)
        if res.status_code==200:
            s1=re.findall(b,res.text)
            if b in s1:
                o=True
                break
else:
    o=False
if o:
    print('Yes')
else:
    print('No') 