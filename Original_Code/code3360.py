def check_date(data):
    data = data.split('.')
    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if 0 < int(data[1]) < 13 and 0 < int(data[0]) <= (month[int(data[1]) - 1]):
        return True
    elif int(data[0]) == 29 and int(data[1]) == 2 and ((int(data[2]) % 4 == 0 and int(data[2]) % 100 != 0) or
                                                       int(data[2]) % 400 == 0 or int(data[2]) % 1000 == 0):
        return True
    else:
        return False

w = 0
data = input()
while data != '.':
    if check_date(data):
        print('Корректная')
        w += 1
    else:
        print('Некорректная')
    data = input()
print(w) 