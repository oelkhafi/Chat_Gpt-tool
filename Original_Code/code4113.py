# put your python code here
a = float(input())
b = float(input())
opr = str(input())
# +, -, /, *, mod, pow, div, где mod — это взятие остатка от деления, pow — возведение в степень, div — целочисленное деление.
if opr == ""+"":
    print(a + b)
elif opr == ""-"":
    print(a - b)
elif opr == ""/"":
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif opr == ""*"":
    print(a * b)
elif opr == ""mod"":
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif opr == ""pow"":
    print(a ** b)
elif opr == ""div"":
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
 