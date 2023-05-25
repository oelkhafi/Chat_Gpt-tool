x = input()
i = 0
s = ''
a = len(x) - 1
b = 1

if len(x) == 1:
    print(x + '1')

while i < a and len(x) > 1:
    if x[i] != x[i + 1]:
        s += x[i] + '1'
        i += 1
    if i >= a:
        break
    while x[i] == x[i + 1]:
        i += 1
        b += 1
        if i >= a:
            break
    s += x[i] + str(b)
    i += 1
    b = 1

if (len(x) > 1) and (x[-1] != x[-2]):
    s += x[-1] + '1'

print(s)
 