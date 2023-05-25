# Posted from PyCharm Edu
import urllib.request
import re

def get_links(url):
    try:
        doc = urllib.request.urlopen(url)
        return re.findall(r'href=[\'\""]([^""]*)[\'\""]', str(doc.read()))
    except:
        return []

url1, url2 = input(), input()

for x in get_links(url1):
    if url2 in get_links(x):
        print('Yes')
        break
else:
    print('No')





 