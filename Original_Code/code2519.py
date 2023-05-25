def fib(n):
	m = []
	m.append([])
	m[0] = 0
	m.append([])
	m[1] = 1	
	i = 2
	f = 0
	while i <= n:
		f = m[i - 1] + m[i - 2]
		m.append([])
		m[i] = f
		i += 1
	if n == 1:
		f = 1
	return(f)
def main():
    n = int(input())
    print(fib(n))

if __name__ == ""__main__"":
    main() 