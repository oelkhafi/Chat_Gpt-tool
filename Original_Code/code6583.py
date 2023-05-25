x1, y1, x2, y2 = map(int, input().split())

area = [(x1, y1)]
if x1 == x2 or y1 == y2:
    print(""YES"")
else:
    x, y = x1, y1
    alpha = 1
    for i in range(16):
        x += alpha
        y += alpha
        area.append((x, y))
        if x == 9 or x == 0 or y == 9 or y == 0:
            alpha *= -1
            
    x, y = x1, y1
    alpha = 1    
    for i in range(16):
        x += alpha
        y -= alpha
        area.append((x, y))
        if x == 9 or x == 0 or y == 9 or y == 0:
            alpha *= -1
            
    if (x2, y2) in area:
        print(""YES"")
    else:
        print(""NO"")

 