import requests, re

#метод, который получает список ссылок на странице
def getURL(link):
    res = requests.get(link)
    #получаем список ссылок
    html_text = res.text
    
    links = re.findall(r'<a.+href=""([^""#]+)""', html_text.replace(""'"", '""'))

    #получаем список сайтов
    site_names = []
    for link in links:
        link = link.lower().replace('ftp://', '').replace('https://', '').replace('http://', '')
        site_name = re.match(r'(\w[^/:_?]+)', link) #r'://([^/:?]+)'
        if site_name is not None:
            #print(site_name[0])
            if site_name[0] not in site_names:
                site_names.append(site_name[0])
    return site_names

link = input()
site_names = getURL(link)
site_names.sort()
for link in site_names:
    print(link)
 