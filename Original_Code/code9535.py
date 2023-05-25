x = float(input())
z = float(input())
y = str(input())

if y == ""*"":
  print(x*z)
elif y == ""/"" and z == 0:
  print(""Деление на 0!"")
elif y == ""/"":
  print(x/z)
elif y == ""-"":
  print(x-z)
elif y == ""+"":
  print(x+z)
elif y == ""mod"" and z == 0:
  print(""Деление на 0!"")
elif y == ""mod"":
  print(x%z)
elif y == ""pow"":
  print(x**z)
elif y == ""div"" and z == 0:
  print(""Деление на 0!"")
elif y == ""div"":
  print(x//z)  
else:
    print(""False"") 