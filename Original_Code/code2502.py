s = input().split()
#print(s)
i = 0
sum = -1
for c in s:
	if len(s) == 1:
		print(s[i])
	else:
		if i == 0:
			#print(s[1]+s[len(s)-1]+""i(start)=""+str(i)) 
			sum = int(s[1])+int(s[len(s)-1])
			print(sum)
			sum = -1
		elif i == len(s)-1:
			#print(s[0]+s[i-1]+""i(stop)=""+str(i))
			sum = int(s[0])+int(s[i-1])
			print(sum)
			sum = -1
		else: 
			#print(s[i-1]+s[i+1]+""i=""+str(i))
			sum = int(s[i-1])+int(s[i+1])
			print(sum)
			sum = -1
	i += 1
 