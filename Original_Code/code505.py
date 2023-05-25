# put your python code here
x, y, op = float(input()), float(input()), input()
if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == 'pow':
    print(x ** y)
elif op == 'mod' and y:
    print(x % y)
elif op == '/' and y:
    print(x / y)
elif op == 'div' and y:
    print(x // y)
else:
    print('Деление на 0!')
    



 