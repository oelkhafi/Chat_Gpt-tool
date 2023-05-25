import requests
import re

A = requests.get(str(input()))
B = str(input())
count = 0
pattern = r""\""(http\S+)\""""
linksOnA = re.findall(pattern, A.text)
for link in linksOnA:
    linksOnC = re.findall(pattern, requests.get(link).text)
    if B in linksOnC:
        print(""Yes"")
        count = 1
        break
if count == 0:
    print(""No"")

    
        
            

 