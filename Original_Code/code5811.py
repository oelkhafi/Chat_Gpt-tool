parents_dictionary = dict()
extended_parents_dictionary = dict()

# читаем ввод, заполняем словарь вида {потомок: [список предков]}
n = int(input())
for _ in range(n):
    input_data = input().split(':')
    if len(input_data) == 1:
        parents_dictionary[input_data[0]] = list()
    else:
        parents_dictionary[input_data[0].split()[0]] = input_data[1].split()

# заполняем расширенный словарь предков
extended_parents_dictionary.update(parents_dictionary)
# добавляем все существующие классы
for child in parents_dictionary.keys():
    for parent in parents_dictionary[child]:
        if parent not in extended_parents_dictionary.keys():
            extended_parents_dictionary[parent] = []
# добавляем в список предков предков предков :)
for child in extended_parents_dictionary.keys():
    for parent in extended_parents_dictionary[child]:
        extended_parents_dictionary[child] += extended_parents_dictionary[parent]

# обрабатываем запросы проверяя есть ли предок в словаре
q = int(input())
for _ in range(q):
    parent, child = input().split()
    if parent == child:
        print('Yes')
    elif parent in extended_parents_dictionary[child]:
        print('Yes')
    else:
        print('No') 