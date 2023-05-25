book = {}
while True:
    i = input()
    if i == '.':
        break
    i = i.split(': ')
    book.update({i[0]: i[1]})
while True:
    i = input()
    if i == '.':
        break
        
    for k, v in book.items():
        if k == i:
            print(book[k])            
        elif book[k] == i:
            print(k)
    
    if i not in book.keys() and i not in book.values():
        print('Нет данных')





 