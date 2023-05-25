# один список ключей, одна функция с указанием направления шифрования
def f_crypt_decrypt(lst, string, crypt=True):
    ret = ''
    if crypt:
        for c in string: ret += ''.join([el[1] for el in lst if c == el[0] ])
    else:
        for c in string: ret += ''.join([el[0] for el in lst if c == el[1] ])
    return ret

key1, key2, str1, str2 = input(), input(), input(), input()

# # для отладки алгоритма
# key1 = 'abcd'         # что нужно заменить
# key2 = '*d%#'         # чем заменить
# str1 = 'abacabadaba'  # *d*%*d*#*d*
# str2 = '#*%*d*%'      # dacabac

lst = list(zip(key1,key2))

print(f_crypt_decrypt(lst, str1))  # шифровка строки
print(f_crypt_decrypt(lst, str2, False)) # дешифровка строки

# этот код лучше версии 4, т.к. используется одна функция и один словарь
#     добавил в функцию 3й параметр, True/False, для указания направления кодирования
#     если функция получила True - кодируем, т.е. меняем lst[el][0] на lst[el][1]
#     а если False - наоборот 