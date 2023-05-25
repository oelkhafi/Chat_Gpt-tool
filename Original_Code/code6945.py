a, b = list(input()), list(input())
a1,b1 = list(input()), list(input())
a2, b2 = [], []
d,d1 = {},{}
i = 0
while i < len(a):
	d[a[i]] = b[i]
	i += 1
i = 0
while i < len(b):
	d1[b[i]] = a[i]
	i += 1	
for i in a1:
	if i in d.keys():
		a2.append(d[i])
for i in b1:
	if i in d1.keys():
		b2.append(d1[i])
for i in a2:
	print(i, end='')
print()
for i in b2:
	print(i, end='') 