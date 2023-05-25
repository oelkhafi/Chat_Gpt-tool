# put your python code here
num1 = float(input())
num2 = float(input())
p = input()

if p in ['mod','div','/'] and num2 == 0.0:
    print('Деление на 0!')
    
elif p == 'mod':
    print(num1 % num2)
elif p == 'pow':
    print(num1 ** num2)
elif p == 'div':
    print(int(num1) // int(num2))    
elif p == '*':
    print(num1 * num2)
elif p == '/':
    print(num1 / num2) 
elif p == '+':
    print(num1 + num2)
elif p == '-':
    print(num1 - num2)    

 