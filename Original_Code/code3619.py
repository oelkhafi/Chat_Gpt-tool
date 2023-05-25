import requests
import re

url_1, url_2  = [input() for i in range(2)]
flag = 0
def get_request(s):
    # Переходим по перрвой ссылке, с помощью get
    res = requests.get('{}'.format(s))
    # Регулярным выраженем, формируем лист сосоящий из гиперссылок 
    pattern = '<a href=""(.+)"">'
    list_hyperlink = re.findall(pattern, res.text)
    return list_hyperlink 
       
for list in get_request(url_1):
    if flag == 0:
        if url_2 in get_request(list):
            print('Yes')
            flag = 1
            break

if flag == 0:
    print('No')
  