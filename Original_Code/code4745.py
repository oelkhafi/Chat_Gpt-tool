n, k = [int(i) for i in input().split()]
a, m = [i for i in range(k)], 1
if k == 1:
	print('\n'.join([str(i) for i in range(n)]))
else:
	while True:
		a[k-1] = -1
		while a[k-1] < n-1:
			a[k-1] += 1
			if len(set(a)) == k:
				print(*a)
		if sum(a) != (n - 1) * k:
			while a[k-m] == a[k-m-1]:
				m += 1
			a[k-m-1] += 1
			for i in range(k-m, k):
				a[i] = 0
			m = 1
		else:
			break
 