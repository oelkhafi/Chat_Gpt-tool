z = 0
s, a, b = input(), input(), input()
while True:
    if a in s:
        c = s.replace(a, b)
        s = c
        z += 1
        if a not in s:
            print(z)
            break
        if a == b or z > 1000:
            print('Impossible')
            break
    else:
        print(0)
        break






 