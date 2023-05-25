import re

str = input()
result = ''
regex = re.findall(r'\d*[a-z]|\d*[A-Z]', str)

for elem in regex:
    qwe = re.findall(r'(\d*)(\w)', elem)
    lst = list(qwe[0])
    if '' in lst:
        lst.remove('')
    if len(lst) == 2:
        e = int(lst[0])*lst[1]
        result = result + e
    else:
        result = result + lst[0]

print(result)




 