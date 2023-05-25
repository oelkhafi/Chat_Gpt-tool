n = int(input())
lst_number = []
for i in range(n):
    n = int(input())
    lst_number.append(n)
a = max(lst_number)
b = min(lst_number)
while b != 0:
    if a == b:
        break
    if b > a:
        a, b = b, a
    a, b = b, a % b
print(a)
if a == 1:
    print(""NO"")
else:
    for j in range(2, a):
        if a % j == 0:
            print(""NO"")
            break
    else:
        print(""YES"")
 