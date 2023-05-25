import sys

buffL_for_print=[]

# запуск функции проверки на число Капрекара(через рекурсию?)
# дополнительная проверка в множестве для 6-ти значных чисел
def kaprekar_check(n):
    nn = str(n)
    num_str=[]

    for i in range(len(nn)):
        num_str.append(int(nn[i]))

    my_set = set(num_str)

    if (len(nn) != 3 and len(nn) != 4 and len(nn) != 6) or (n == 100 or n == 1000 or n == 100000 or len(my_set) == 1):
        print(""Ошибка! На вход подано число "" +str(n)+"", не удовлетворяющее условиям процесса Капрекара"")
        sys.exit()    
    else:
        return (n)


#  Напишите функцию numerics(n), принимающую на вход 1 натуральное число, 
#  а возвращающую список цифр из которых состоит число
def numerics(n):
    L=[]
    nums = str(n)
    for i in range(len(nums)):
        L.append(int(nums[i]))
    return L


#  Функция должна сформировать внутри 2 числа:
def kaprekar_step(L):    
    nums = L
    # проверка нахождения ответа списке, выход при нахождении элемента в списке
    if str(L) not in buffL_for_print: # формируем список всех пробегающих чисел
        buffL_for_print.append(str(L))# формируем множество уникальных чисел
    else:
        for i in range(len(buffL_for_print)):# вывод уникальных чисел из множества и завершение п-мы
            
            buff_num = buffL_for_print[i]
            buff_num = buff_num[1:-1]
            buff_num = buff_num.replace("","","""")
            buff_num = buff_num.replace("" "","""")
            print(int(buff_num))
            buff_num = int(buff_num)
            
            L_for_print = int(''.join([str(i) for i in nums]))
            
            if (buff_num == 495 or buff_num == 6174 or buff_num == 549945 or buff_num == 631764):
                sys.exit()
            
        print(""Следующее число - ""+str(L_for_print)+"", кажется процесс зациклился..."")
        sys.exit()
        
    a = int(''.join([str(i) for i in (sorted(nums, reverse=True))]))
    b = int("""".join([str(i) for i in (sorted(nums))]))
    x = a - b
    return x

# конечная функция
def kaprekar_loop(n):
    n = kaprekar_check(n) # зачем возвращать True or False, если я их не буду использовать?
    L = numerics(n)# принимает число n, возвращает список цифр n
    x = kaprekar_step(L) # принимает L- список чисел, возвращает разницу между макс и мин
    kaprekar_loop(x)

#n = 103303
#kaprekar_loop(n) 