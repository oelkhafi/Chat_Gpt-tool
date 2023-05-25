import requests
import re

A = input()
B = input()


def get_urls(url):
    page = requests.get(url)
    data = page.text
    pattern = r""href=['\""]?([^'\"" >]+)""
    urls = re.findall(pattern, data)
    return urls


for url in get_urls(A):
    if B in get_urls(url):
        print('Yes')
        break
else:
    print('No')
 