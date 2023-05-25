import json


# Функция проверяет являетя ли класс 1 предком класса 2
def is_parent (class1, class2):
  if class2 in parents.keys():
    if class1 in parents[class2]: 
      return True
    else: 
      for i in parents[class2]:
        if is_parent(class1,i) == True: return True

# Получаем данные в формате json и переводим их в формат python
data_json = input().strip()
data = json.loads(data_json)

# Создаем и заполняем словарь {класс : прямые предки}, а также создаем список классов ['A', 'B', 'C', ...]:
parents = {}
classes = []
for i in data:
  parents[i['name']] = i['parents']
  classes.append(i['name'])

# Считаем и выводим для каждого класса количество потомков:
for i in sorted(classes):
  counter = 0
  for j in classes:
    if i == j: counter += 1
    elif is_parent(i, j): counter += 1
  print(i,':',counter) 