# тестовые значения
#m = [[9, 5, 3],[0, 7, -1], [-5, 2, 9]]
#f = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

#m = [[1]]
#f = [[-1]]

# заполнение двумерного массива
m = []
f = []

ii = 0
while True:
	s = [str (i) for i in input().split()]
	###print(""->"" + str(s[len(s)-1]))
	if s[len(s)-1] == ""end"":
		break
	else:
		m.append([])
		f.append([])
		for j in range(0, len(s)):
			m[ii].append(s[j])
			f[ii].append(-1)
	ii += 1	
	
row = ii-1	
col = j
###print(row, ""\t"", col)

'''
# вывод двумерного массива
print (""---------------------"")
for i in range (len (m) ):
	for j in range (len (m[i]) ):
		print (m[i][j], end =""\t"")
	print ()
# вывод двумерного массива
print (""---------------------"")
for i in range (len (m) ):
	for j in range (len (m[i]) ):
		print (f[i][j], end =""\t"")
	print ()	
row = i
col= j
print (""---------------------"")	
print(row, ""\t"", col)

'''
# обработка двумерного массива по заданию
i1=-1
j1=-1
for i in range (len (m) ):
	for j in range (len (m[i]) ):
		i1 = i
		j1 = j
		
		if i == 0: 
			m1 = m[row][j1]
		else:
			m1 = m[i1-1][j1]  # 1е слагаемое 
		###print (""m1="" + str(m1))
		
		if i == row:
			m2 = m[0][j1]
		else:
			m2 = m[i1+1][j1]  # 2е слагаемое
		###print (""m2="" + str(m2))
		
		if j == 0:
			m3 = m[i1][col]
		else:
			m3 = m[i1][j1-1]  # 3е слагаемое
		###print (""m3="" + str(m3))
		
		if j == col:
			m4 = m[i1][0]
		else:
			m4 = m[i1][j1+1]  # 4е слагаемое
		###print (""m4="" + str(m4))
			
		f[i][j] = int(m1) + int(m2) + int(m3) + int(m4)
		###print (str(m1) + ""|"" + str(m2) + ""|"" + str(m3) + ""|"" + str(m4))
	###print()

# вывод двумерного массива
###print (""---------------------"")
for i in range (len (m) ):
	for j in range (len (m[i]) ):
		print (f[i][j], end =""\t"")
	print ()
###print (""---------------------"")	
 