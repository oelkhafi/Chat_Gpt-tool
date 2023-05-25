# put your python code here
A= float(input())
B= float(input())
O= str(input())
if O==""+"":
    print(A+B)
elif O==""-"":
    print(A-B)
elif O==""*"":
    print(A*B)
elif O==""/"":
    if B!=0:
        print(A/B)
    else:
        print(""Деление на 0!"")
elif O==""mod"":
    if B!=0:
        print(A%B)
    else:
        print(""Деление на 0!"")
elif O==""div"":
    if B!=0:
        print(A//B)
    else:
        print(""Деление на 0!"")
elif O==""pow"":
    print(A**B) 