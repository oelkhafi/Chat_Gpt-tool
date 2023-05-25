def encripter(dict_encripter, mess):
    """"""Шифрует строку""""""
    res_string = ''
    for id, item in enumerate(mess):
        for key, value in dict_encripter.items():
            if item == key:
                res_string += value
    return res_string

def decripter(dict_encripter, mess):
    """"""Расшифровывает строку""""""
    res_string = ''
    for id, item in enumerate(mess):
        for key, value in dict_encripter.items():
            if item == value:
                res_string += key
    return res_string
   
string = list(input())
capher = list(input())
need_to_encrypt = input()
need_to_decrypt = input()
dict_encripter = dict(zip (string, capher))
print(encripter(dict_encripter, need_to_encrypt))
print(decripter(dict_encripter, need_to_decrypt)) 