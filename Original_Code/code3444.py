# put your python code here
import json
data = json.loads(input())
dict_answer, dict2 = {}, {}
# создаем словарь предок: [потомки]
for el in data:
    if el['parents'] == [] and el['name'] not in dict2:
        dict2[el['name']] = [el['name']]
    else:
        for i in el['parents']:
            if i not in dict2:
                dict2[i] = [el['name']]
            else:
                dict2[i] += [el['name']]
# добавляем не попавших предков
for elem in data:
    if elem['name'] not in dict2:
        dict2[elem['name']] = [elem['name']]
# функция-рекурсия в глубину        
def find_path(start, path):
    path.add(start)
    for node in dict2[start]:
        if node not in path and node in dict2:
            find_path(node, path)
        else:
            path.add(node)
# добавляем ответы в словарь с ответами)
for i in dict2:
    way = set()
    find_path(i, way)
    dict_answer[i] = len(way)
# сортируем и выводим словарь с ответами
for key, value in sorted(dict_answer.items()):
    print(key, ':', value) 