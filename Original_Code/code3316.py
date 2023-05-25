n = int(input())
max = int(input())
min = max
bufer = 0
for i in range(n - 1):
    number = int(input())
    if number > max:
        max = number
    if number < min:
        min = number
while min != 0 and max != 0:
    if max > min:
        max %= min
    else:
        min %= max
nod = min + max
print(nod)
if nod == 1:
    print(""NO"")
else:
    for i in range(2, nod - 1):
        if (max + min) % i == 0:
            bufer = 1
    print(""NO"" if bufer else ""YES"")
 