strings = 'sab'
value_string = {}
cnt = 0
for i in range(3):
    value_string[strings[i]] = str(input())

while cnt <= 1001:
    if cnt <= 1000:
        if value_string['s'].lower().count(value_string['a']) > 0:
            value_string['s'] = value_string['s'].replace(value_string['a'], value_string['b'])
            cnt += 1
        else:
            print(cnt)
            break
    else:
        print('Impossible')
        break




 