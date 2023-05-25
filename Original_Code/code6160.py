def visokos(y):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):        
        return True
    else:
        return False
    

def check_date(d=0, m=0, y=0):
    if m > 12 or m < 0:
        answer = 'Некорректная'
        return(answer)
    elif m in [4, 6 ,9 ,11] and d > 30:
        answer = 'Некорректная'
        return(answer)
    elif m == 2 and visokos(y) == False and d > 28:
        answer = 'Некорректная'
        return(answer)
    elif m == 2 and visokos(y) == True and d > 29:
        answer = 'Некорректная'
        return(answer)
    elif d > 31:
        answer = 'Некорректная'
        return(answer)
    else:
        answer = 'Корректная'
        return(answer)    
    
cor = 0
while True:    
    string = input()
    if string == '.':
        print(cor)
        break
    date = [int(i) for i in string.split('.')]
    if check_date(*date) == 'Корректная':
        cor += 1        
        print('Корректная')
    else:    
        print('Некорректная')

 