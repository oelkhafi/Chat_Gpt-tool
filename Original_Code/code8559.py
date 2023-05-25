a = float(input())
b = float(input())
znak = input()
if znak == '+':
    print(a + b)
elif znak == '-':
    print(a - b)
elif znak == '*':
    print(a * b)
elif znak == '/':
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Деление на 0!')
        
elif znak == 'mod':
    try:
        print(a % b)
    except ZeroDivisionError:
        print('Деление на 0!')
elif znak == 'pow':
    print(a ** b)
    
elif znak == 'div':
     try:
        print(a // b)
     except ZeroDivisionError:
        print('Деление на 0!')
 