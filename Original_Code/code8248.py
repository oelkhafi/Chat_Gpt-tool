# put your python code here
o1, o2, z = float(input()), float(input()), input()
if z == ""+"":
    print(o1 + o2)
elif z == ""-"":
    print(o1 - o2)
elif z == ""*"":
    print(o1 * o2)
elif z == ""pow"":
    print(o1 ** o2)
else:
    if o2 == 0:
        print(""Деление на 0!"")
    else:
        if z == ""/"":
            print(o1 / o2)
        if z == ""mod"":
            print(o1 % o2)
        if z == ""div"":
            print(o1 // o2)




 