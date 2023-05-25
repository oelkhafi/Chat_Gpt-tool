password = input()
result = 'Good password'
buffer = 10
if '0' not in password:
    buffer -= 1
if '1' not in password:
    buffer -= 1
if '2' not in password:
    buffer -= 1
if '3' not in password:
    buffer -= 1
if '4' not in password:
    buffer -= 1
if '5' not in password:
    buffer -= 1
if '6' not in password:
    buffer -= 1
if '7' not in password:
    buffer -= 1
if '8' not in password:
    buffer -= 1
if '9' not in password:
    buffer -= 1
if 'qwerty' in password or '1234' in password:
    result = 'Bad password'
if len(password) < 8 or buffer == 0:
    result = 'Bad password'
print(result)
 