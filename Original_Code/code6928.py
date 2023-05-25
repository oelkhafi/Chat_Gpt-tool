# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(end = '\t')

for e in range(c, d + 1):
	print(e, end = '\t')

print()

for q in range(a, b + 1):
	print(q, end='\t')
	for w in range(c, d + 1):
				print(q * w, end = '\t')
	print()



 