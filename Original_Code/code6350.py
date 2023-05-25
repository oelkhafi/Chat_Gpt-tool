# put your python code here
num1 = float(input())
num2 = float(input())
op = input()
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print(""Деление на 0!"")
elif op == '*':
    print(num1 * num2)
elif op == 'mod':
    if num2 != 0:
        print(num1 % num2)
    else:
        print(""Деление на 0!"")
elif op == 'pow':
    print(num1 ** num2)
elif op == 'div':
    if num2 != 0:
        print(num1 // num2)
    else:
        print(""Деление на 0!"")
 