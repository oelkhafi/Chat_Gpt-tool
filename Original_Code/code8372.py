import re
import requests

pat = r'href\s*=\s*[\'""](.+?)[\'""]'  # на основе регулярки и таблицы, разясняющей её работу в https://msdn.microsoft.com/ru-ru/library/t9e807fx(v=vs.110).aspx?cs-save-lang=1&cs-lang=vb#code-snippet-1

lst = [input(), input()]  # раскомментировать для сдачи задания

try:
    resA = requests.get(lst[0])
except:
    print('No')

dct = {}  # словарь ссылок: 0й уровень содержит прямые ссылки из документа А,
#                           1й уровень содержит ссылки из документов 0го уровня
#           после заполнения проверим 1й уровень и если обнаружим там ссылку на документ Б
#           печатаем ДА иначе НЕТ

if resA.status_code == 200:
    match = re.findall(pat, resA.text, re.IGNORECASE)
    dct[0] = match if match else []

for ref in dct.get(0, []):
    try:
        resC = requests.get(ref)
        if resC.status_code == 200:
            dct[1] = dct.get(1, []) + re.findall(pat, resC.text, re.IGNORECASE)
    except:
        continue

print('Yes' if lst[1] in dct.get(1, []) else 'No') 