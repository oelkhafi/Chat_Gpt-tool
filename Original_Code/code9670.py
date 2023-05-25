import requests
import re
urlA = input().strip()
urlB = input().strip()
#urlA = ""https://stepic.org/media/attachments/lesson/24472/sample1.html""
#urlB = ""https://stepic.org/media/attachments/lesson/24472/sample2.html""

respA = requests.get(urlA)
respB = requests.get(urlB)
header_typeA = str.lower(respA.headers[""Content-Type""]).split(sep="";"")[0]
header_typeB = str.lower(respB.headers[""Content-Type""]).split(sep="";"")[0]

if header_typeA != ""text/html"" or header_typeA != ""text/html"":
    print(""No"")

textA = respA.text
textB = respB.text
ref_urlsA = re.findall(""href=\""(.*)\"""", textA)
ref_urlsB = re.findall(""href=\""(.*)\"""", textB)
#print(ref_urlsA)
#print(ref_urlsB)

links_in_C = dict()
for ref_urlA in ref_urlsA:
    resp = requests.get(ref_urlA)
    header = resp.headers[""Content-Type""].split(sep="";"")[0]
    if resp.status_code != 200 or header != ""text/html"":
        continue
    urls = re.findall(""href=\""(.*)\"""", resp.text)
    links_in_C[ref_urlA] = urls

condition = ""No""

for linkC in links_in_C:
    links = links_in_C[linkC]
    for link in links:
        if link == urlB:
            condition = ""Yes""
            break
    if condition == ""Yes"":
        break
print(condition) 