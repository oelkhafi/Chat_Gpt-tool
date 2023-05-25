# Даны целые числа 1≤n≤10(18) и 2≤m≤10(5),
# необходимо найти остаток от деления
# n-го числа Фибоначчи на m.
# 10(5)  = 100000
# 10(18) = 1000000000000000000

def fib(n,m):
    d = [0,1]
    a,b=0,1
    f = 0
    
    for i in range(0,6*m):
        f = d[i] + d[i+1]
        d.append(f%m)
        if d[len(d)-1]==1 and d[len(d)-2]==0:
            break
            
    for j in range(n%(len(d)-2)): a, b = (a+b), a
    return a%m

def main():
    n, m = map(int, input().split())
    print(fib(n, m))


if __name__ == ""__main__"":
    main()
 