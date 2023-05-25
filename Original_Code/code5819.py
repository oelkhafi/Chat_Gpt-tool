import re
import requests

url_a = input()
url_b = input()

pattern = r'https.*html'
two_transitions = False

r = requests.get(url_a)
links_in_a = re.findall(pattern, r.text)

for url in links_in_a:
    r = requests.get(url)
    links_in_c = re.findall(pattern, r.text)
    if url_b in links_in_c:
        two_transitions = True

if two_transitions:
    print('Yes')
else:
    print('No') 