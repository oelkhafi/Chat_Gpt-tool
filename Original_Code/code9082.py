import requests
import re


def find_way(source, target, depth=2):
    if depth == 0:
        return False

    res = requests.get(source)
    if res.status_code != 200:
        return False

    links = re.findall(r'<a href=""(.*?)"".*>.*<\/a>', res.text)
    if target in links and depth == 1:
        return True

    for link in links:
        if find_way(link, target, depth - 1):
            return True
        
    return False


s, t = input(), input()
print('Yes' if find_way(s, t) else 'No')
 