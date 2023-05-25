# put your python code here
a =[int(i) for i in input().split()]

if len(a) == 1:
	print(a[0])

if len(a) > 1:
	for i in range(len(a)):
		s = 0
		if i == 0:
			s = a[i+1] + a[-1]
			print(s, end=' ')
			continue
		if i == (len(a) - 1):
			s = a[0] + a[-2]
			print(s, end=' ')
			break
		s = a[i-1] + a[i+1]
		print(s, end=' ')

	



 