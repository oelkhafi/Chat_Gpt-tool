from math import pow, fmod
A = float(input())
B = float(input())
oper = input()
if (B == 0 and (oper == ""/"" or oper == ""div"" or oper == ""mod"")):
    print(""Деление на 0!"")
elif oper == ""+"":
    print(A + B)
elif oper == ""-"":
    print(A - B)
elif oper == ""/"":
    print(A / B) 
elif oper == ""*"":
    print(A * B)
elif oper == ""mod"":
    print(fmod(A, B))
elif oper == ""pow"":
    print( pow(A, B))
elif oper == ""div"":
    print(A // B)




 