classes = {}

def func(predok, potomok):
    if predok in classes.keys() and potomok in classes.keys():
        if predok == potomok or predok in classes[potomok]:
            return 'Yes'
        else:
            for i in range(len(classes[potomok])):
                if func(predok, classes[potomok][i]) == 'Yes':
                    return func(predok, classes[potomok][i])
                else:
                    continue
    return 'No'

for i in range(int(input())):
    s = input()
    if ':' not in s:
        key, value = s, ''
    else:
        key, value = s.split(' : ')
    classes.update({key : value.split()})

test = [input().split() for j in range(int(input()))]

for x, y in test:
    print(func(x, y)) 