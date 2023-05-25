a = input().split()
x = 0
y = 0
s = 1
for i in a:
    if i == 'l':
        x -= 1
    elif i == 'r':
        x += 1
    elif i == 'u':
        y += 1
    elif i == 'd':
        y -= 1
    elif i == '*':
        s += 1
    elif i == '#':
        s -= 1
    if s == 0:
        break
print(x, y)
print(s) 