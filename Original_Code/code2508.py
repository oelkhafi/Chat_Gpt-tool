# Ввод размерности матрицы
n = int(input())
# Создание и заполнение матрицы нулями
m = [[i*0 for i in range(n)] for i in range(n)]
# Обработка матрицы
a = n*n
i = 0
j = -1
r = n
s = 0
while s < a:
	#r 
	k = 1
	while k <= r:
		j += 1
		s += 1
		m[i][j] = s
		k += 1
	d = r - 1
	#d
	k = 1
	while k <= d:
		i += 1
		s += 1
		m[i][j] = s
		k += 1
	l = d 
	#l
	k = 1
	while k <= l:
		j -= 1
		s += 1
		m[i][j] = s
		k += 1
	u = l - 1
	#u
	k = 1
	while k <= u:
		i -= 1
		s += 1
		m[i][j] = s
		k += 1
	r = u
# Вывод матрицы
for i in range (len(m)):
	for j in range (len(m[i])):
		print(m[i][j], end =""\t"")
	print()
 