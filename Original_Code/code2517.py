def ff(x):
	r = ''
	#print('----------------------------------------')
	#print(d)
	#print('----------------------------------------')	
	for key in sorted(d.keys()):
		if str(key) == str(x):
			r = str(d[key])
			#rr = str(r) + ""++""
			break
	if r == '':
		d[x] = f(x)
		r = d[x]
		#rr = str(r) + ""+""
	#return(rr)
	return(r)

d = {}

x = int(input())
for i in range (1,x+1):
	y = int(input())
	print(ff(y))
 