import requests
import re

def get_urls(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    string = r.text
    pattern = r'<a href=""(http.*)"">'
    return re.findall(pattern, string)

url_A = input()
url_B = input()

ans = 'No'
lst_A = get_urls(url_A)
for url in lst_A:
    try:
        lst_B = get_urls(url)
        if url_B in lst_B:
            ans = 'Yes'
            break
    except TypeError:
        pass
print(ans)
 