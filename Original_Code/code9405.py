import requests, re

def Get_URL_list(res):
    result = [] 
    if res.status_code != 200:
        return result
    reg = re.findall(r""<a href=\""(.*)\"""", res.text)
    for link in reg:
        result.append(link)
    return result

def Check_URLs(urlA, urlB):
    result = False
    for urlA2 in Get_URL_list(requests.get(urlA)):
        if urlB in Get_URL_list(requests.get(urlA2)):
            result = True
    return result

urlA = input()
urlB = input()

print('Yes' if Check_URLs(urlA, urlB) else 'No') 