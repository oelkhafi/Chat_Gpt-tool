# Функция проверки на родительство:
def is_parent (class1, class2):
  if class2 in parents.keys():
    if class1 in parents[class2]: 
      return True
    else: 
      for i in parents[class2]:
        if is_parent(class1,i) == True: return True


# Создаем и заполняем словарь {класс исключений: его предки}
parents = {} 
for i in range(int(input())):
  temp = input().split()
  parents[temp[0]] = temp[2:]

# Заполняем список в порядке, в котором в программе записаны исключения:
Order = [] 
for i in range(int(input())):
  Order.append(input())

# Проверяем:
for i in range(len(Order)): # цикл по исключениям, записанным в программном коде 
  if Order.index(Order[i]) < i: #  Если ранее в списке стоит точно такое же исключение!!!
    print (Order[i])
    break
  for j in range(i): # цикл по исключениям, стоящим до i-го элемента
    if is_parent (Order[j], Order[i]) == True:
      print (Order[i])
      break 