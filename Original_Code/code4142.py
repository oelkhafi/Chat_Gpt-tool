enigma_key = {}


def enigma():
    for i in range(len(key_in)):
        enigma_key.setdefault(key_in[i], value_in[i])


def encode(to_encode_line):
    encode_line = ''
    for i in to_encode_line:
        encode_line += enigma_key[i]
    return encode_line


def decode(to_decode_line):
    decode_line = ''
    for i in (to_decode_line):
        for key, value in enigma_key.items():
            if i == value:
                decode_line += key
    return decode_line


key_in = str(input())
value_in = str(input())
while len(key_in) != len(value_in):
    print('Вы ввели строки разной длинны, повторите ввод!')
    key_in = str(input('введите ключ строку: '))
    value_in = str(input('введите значение : '))
to_encode_line = str(input())
to_decode_line = str(input())
enigma()
print(encode(to_encode_line))
print(decode(to_decode_line))
 