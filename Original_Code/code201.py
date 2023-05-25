a = float(input())
b = float(input())
s = input()
if s == ""+"":
	print(a+b)
elif s == ""-"":
	print(a-b)
elif s == ""*"":
	print(a*b)
elif s == ""pow"":
	print(a**b)
elif b == 0:
	print(""Деление на 0!"")
elif s == ""/"":
	print(a/b)
elif s == ""div"":
	print(a//b)
else:
	print(a%b)




 