figure = input()

if figure == 'треугольник':
    n = 3
elif figure == 'прямоугольник':
    n = 2
elif figure == 'круг':
    n = 1
    
d = []
for i in range(n):
    d.append(float(input()))    

if len(d) == 3:
    p = (d[0] + d[1] + d[2]) / 2
    s = (p * (p - d[0]) * (p - d[1]) * (p - d[2])) ** 0.5
if len(d) == 2:
    s = d[0] * d[1]
if len(d) == 1:
    s = 3.14 * (d[0] ** 2)

print(s)
 