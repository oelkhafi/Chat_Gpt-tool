files = {}
while True:
    string = input()
    if string == '.':
        break
    string = string.split()
    files[string[0]] = string[1]
while True:
    string = input()
    if string == '.':
        break
    string = string.split()
    if string[2] == 'admin':
        print('Access granted')
    if string[2] == 'experienced':
        if string[1] == 'read' and files[string[0]] != 'confidential':
            print('Access granted')
        elif string[1] == 'edit' and files[string[0]] not in ['settings', 'system']:
            print('Access granted')
        else:
            print('Access denied')
    if string[2] == 'user':
        if files[string[0]] == 'ordinary':
            print('Access granted')
        else:
            print('Access denied')
 