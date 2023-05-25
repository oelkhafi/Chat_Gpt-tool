import requests, re

#метод, который получает список ссылок на странице
def getURL(link):
    res = requests.get(link)
    #получаем список ссылок
    html_text = res.text
    links = re.findall(r'<a href=""(http[^""#]+)""', html_text)
    #проверяе каждую ссылку на доступность
    good_links = []
    for link in links:
        if requests.get(link).status_code == 200:
            good_links.append(link)
    return good_links

def checkLink(link_end, links):
    if len(links) == 0:
        return False
    else:
        for link in links:
            if link_end == link:
                return True
    return False


link_start = input() #""https://stepic.org/media/attachments/lesson/24472/sample0.html""
link_end = input() #""https://stepic.org/media/attachments/lesson/24472/sample2.html""
links1 = getURL(link_start)
yes = False
for link1 in links1:
    links2 = getURL(link1)
    if checkLink(link_end, links2):
        yes = True
        break
if yes:
    print('Yes')
else:
    print('No')

 