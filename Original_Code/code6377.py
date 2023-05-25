#1 Начальные данные
x, y, dx, dy  = 0, 0, 0, 0
commands, courses, distances = [], [], []
turtle = [[],[]]   # список координат черепашки
#2 Ввод данных
steps = int(input())
for i in range(steps):
    way = input().strip().split()
    way[1] = int(way[1])
    commands.append(way)
#2 Списки курсов и расстояний
for i in range(steps):
    courses.append(commands[i][0])
    distances.append(commands[i][1])
#3 Направления
course = {'север': 1, 'запад': -1, 'юг': -1, 'восток': 1}
#4 Передвижения
for i in range(steps):
    if courses[i % steps] == 'восток' or courses[i % steps] == 'запад':
        dx += course[courses[i % steps]] * distances[i % steps]
        turtle[0].append(x + dx)
        turtle[1].append(y + dy)
    elif courses[i % steps] == 'север' or courses[i % steps] == 'юг':
        dy += course[courses[i % steps]] * distances[i % steps]
        turtle[0].append(x + dx)
        turtle[1].append(y + dy)
#6 Выходные данные
print(turtle[0][i], turtle[1][i], end = '') 