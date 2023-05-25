# Функция добавления пространства имен в глобальный список nslist
def nslist_mod (now_list, new_ns, parent_ns):
  for i in now_list:
    if i == parent_ns: #если нашли список (пространство) в котором надо создать новый спискок (подпространство)
      now_list.append([new_ns]) # то создаем его
      return now_list
    elif type(i) == list: # если список не родительский, то заходим в него и ищем уже в нем с помощью рекурсии
        answer = nslist_mod(i, new_ns, parent_ns)
        if answer != None:    
          now_list.remove(i)
          now_list.append(answer)
          return now_list

# Функция добавления переменных в глобальный список nslist
def nslist_add (now_list, parent_ns, var):
  for i in now_list:
    if i == parent_ns: # если нашли список (пространство), в которое надо записать переменную
      now_list.append(var) # то добавляем ее в список (пространство)
      return now_list
    elif type(i) == list: # если список (пространство) не родительское, то заходим в него и ищем уже в нем с помощью рекурсии
        answer = nslist_add(i, parent_ns, var)
        if answer != None:    
          now_list.remove(i)
          now_list.append(answer)
          return now_list

# Функция поиска переменных в пространствах имен
def nslist_get (now_list, asked_ns, var):
  if now_list[0] == asked_ns and var in now_list: return now_list[0] # если искомая переменная находится в заданном списке (пространстве), то return 'название списка' и возвращаемся в родительское пространство
  elif now_list[0] == asked_ns and var not in now_list: return 0 # если найден заданный список, а переменной в нем нет, то return 0 и возвращаемся в родительский список (пространство)
  else: # если заданный список (пространство) еще не найден, то продолжаем перебирать списки и уходить вглубь каждого из них с помощью рекурсии, пока не найдем заданный список (пространство)
    for i in now_list:
      if type(i) == list:
        answer = nslist_get (i, asked_ns, var)
        if answer == 0:
          if var in now_list: return now_list[0]
          else: return 0
        elif answer != None: return answer

# ОСНОВНОЙ КОД ПРОГРАММЫ:
nslist = ['global'] # список вложенных списков имитирующий структуру пространств имен и переменных в нем
'''
Например, для команд из условия задачи список nslist будет выглядеть так:
nslist = ['global', 'a', ['foo', 'b', ['bar', 'a']]]
'''
for i in range(int(input())):
  command = input().split()

  if command[0] == ('create'): # если поступила команда создать пространство имен
    nslist = nslist_mod(nslist, command[1], command[2]) #то обращаемся к функции nslist_mod
  
  elif command[0] == ('add'): # если поступила команда создать переменную
    nslist = nslist_add(nslist, command[1], command[2]) #то обращаемся к функции nslist_add
   
  elif command[0] == ('get'): # если поступила команда найти принадлежность переменной
    answer = nslist_get (nslist, command[1], command[2]) #то обращаемся к функции nslist_get
    if answer == 0: print ('None')
    else: print (answer) 