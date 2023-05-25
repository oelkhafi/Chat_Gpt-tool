import requests
import re


str_1 = re.sub(r""(.+)\n"", r""\1"", input())#input().split()
str_2 = re.sub(r""(.+)\n"", r""\1"", input())#input().split()

res = requests.get(str_1)
list_x = re.findall(r""<a href=\""(https?[^>]+)\"">.+?<\/a>"", str(res.content))

i_cnt_yes = 0
for i in list_x:
    if requests.get(i).status_code == 200:
        list_y = re.findall(r""<a href=\""(https?[^>]+)\"">.+?<\/a>"", str(requests.get(i).content))
        if str_2 in list_y:
            i_cnt_yes += 1
            break

if i_cnt_yes > 0:
    print(""Yes"")
else:
    print(""No"") 