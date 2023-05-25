a = float(input())
b = float(input())
x = input("""")

if (b == 0 and x == ""/""):
  print('Деление на 0!')

if (x == ""/"" and b != 0):
  print(a / b)

if (x == ""+""):
  print(a + b)

if (x == ""-""):
  print(a - b)
  
if (x == ""*""):
  print(a * b)
  
if (x == ""mod""):
  if(b == 0):
    print('Деление на 0!')
  else:
    print(int(a % b))
  
if (x == ""pow""):
  print(a ** b)
  
if (x == ""div""):
   if(b == 0):
     print('Деление на 0!')
   else:
     print(a // b) 