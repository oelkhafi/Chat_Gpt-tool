# put your python code here
n1 = float(input())
n2 = float(input())
operation = input()


if (operation == '+'):
    print(n1 + n2)
elif (operation == '-'):
    print(n1 - n2)
elif (operation == '/' and n2 != 0):
    print(n1 / n2)
elif (operation == '*'):
    print(n1 * n2)
elif (operation == 'mod' and n2 != 0):
    print(n1 % n2)
elif (operation == 'pow'):
    print(n1 ** n2)
elif (operation == 'div' and n2 != 0):
    print(n1 // n2)
else:
    print('Деление на 0!') 