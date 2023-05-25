a=str(input())
if int(a)>=0: a=a[0:]
else: a=a[1:] # Избавляемся от знака [минус], тип str

b=(a) # Переменная b для постановки в print без знака [минус]

a=a[-2:]  # Правсимв(a;2), тип  str
if int(a)>20:
    a=a[-1:] # Правсимв (a;1), тип str
    if int(a)in [1]: print(b,'программист')
    elif int(a) in [2,3,4]: print(b,'программиста')
    else: print(b,'программистов')
else:  # Значение a = 2 символа справа строка 7, тип str
    if int(a)in [1]: print(b,'программист')
    elif int(a) in [2,3,4]: print(b,'программиста')
    else: print(b,'программистов')




 