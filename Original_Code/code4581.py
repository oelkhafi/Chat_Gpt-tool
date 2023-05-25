def check_number(n):
    matrix = '+- ()1234567890'
    digits = 0
    if n.startswith('+7') or n.startswith('8'):
        for counter in n:
            if counter not in matrix:
                return False
            if counter in '1234567890':
                digits +=1
        if digits != 11:
            return False
        else:
            return True
    else:
        return False

def mod_number(n):
    n = n.replace('+', '').replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
    number = '+7 (' + n[1:4] + ') ' + n[4:7] + '-' + n[7:9] + '-' + n[9:]
    return number

phonebook = {}
for counter in iter(input, '.'):
    if ' ' in counter:
        if counter.split()[0] not in phonebook:
            phonebook[counter.split()[0]] = []
        phones = counter.split(maxsplit = 1)[1]
        for phone in phones.split(', '):
            if check_number(phone):
                phonebook[counter.split()[0]].append(mod_number(phone))
    else:
        if counter.split()[0] not in phonebook or phonebook[counter.split()[0]] == []:
            print('Не найдено')
        else:
            print(*phonebook[counter.split()[0]], sep = ', ')
 