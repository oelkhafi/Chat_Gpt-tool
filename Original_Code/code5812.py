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

# преобразуем списки  в множества
for key, value in extended_parents_dictionary.items():
    extended_parents_dictionary[key] = set(value)

exceptions = []
unnecessary_exceptions = []
m = int(input())
for _ in range(m):
    exceptions.append(input())

# проходимся по списку исключений в обратном порядке, выбираем исключение и проверяем
# нет ли среди предыдущих его предков, если есть и исключение еще не добавлено в список
# лишних - то добавляем его, затем печатаем перевернутый список лишних исключений
for _ in range(len(exceptions) - 1, -1, -1):
    unnecessary_exception = exceptions[_]
    for __ in range(_, -1, -1):
        checked_exception = exceptions[__]
        if exceptions.index(unnecessary_exception) == exceptions.index(checked_exception):
            continue
        else:
            if checked_exception in extended_parents_dictionary[unnecessary_exception]\
                    and unnecessary_exception not in unnecessary_exceptions:
                unnecessary_exceptions.append(unnecessary_exception)

unnecessary_exceptions.reverse()
for unnecessary_exception in unnecessary_exceptions:
    print(unnecessary_exception) 