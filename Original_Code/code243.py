a = float(input())
b = float(input())
s = input()
ss = 0
if s == '+':
    ss = a+b
elif s == '-':
    ss = a-b
elif s == '*':
    ss = a*b
elif s == 'pow':
    ss = a**b
elif b == 0:
    ss = 'Деление на 0!'
elif s == '/':
    ss = a/b
elif s == 'div':
    ss = a//b
else:
    ss == a % b
print(ss) 