# put your python code here
n = int(input())
scopes = {'global': {'parent': 'None', 'vars': []}}      #Создаем словарь словарей(сразу вписываю global по-умолчанию)
def findParent(nmspc, arg):                              #Функция поиска пространства имен
            if nmspc in scopes.keys():                   #Проверяем есть ли введенное простанство в списке scopes
                if arg in scopes[nmspc]['vars']:         #Проверяем есть ли введенная переменная в указанном 
                                                         #словаре простр-ва имен nmspc
                    return nmspc
                else:                                    #Если не нашли, то
                    nmspc = scopes.get(nmspc)['parent']  #Присваиваем в nmspc простр-во имен, где искали переменную 
                                                         #и не нашли(на уровень выше)
                    x = findParent(nmspc, arg)           #Запускаем функцию по новой (рекурсия) и так до самого верхнего уровня
                    return x
for i in range(n):
    cmd, nmspc, arg = input().split()
    if cmd == 'add':
        scopes[nmspc]['vars'].append(arg)
    elif cmd == 'create':
        scopes[nmspc] = {'parent': arg, 'vars': []}
    elif cmd == 'get':
        res = findParent(nmspc, arg)
        print(res) 