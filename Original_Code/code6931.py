s = input()
c = 1
if len(s) == 1:
	print(s + str(c))
else:
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			c += 1
			continue
		print(s[i] + str(c), end='')

		if s[i] != s[i+1]:
			c = 1

	print(s[i+1] + str(c))
	
	



 