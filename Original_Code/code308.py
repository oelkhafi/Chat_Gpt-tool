def calc():
    n = int(input())
    d = [0, 0]
    
    for i in range(2, n + 1):
        if i % 3 == 0:
            x3 = d[i // 3] + 1
        else:
            x3 = float('inf')

        if i % 2 == 0:
            x2 = d[i // 2] + 1
        else:
            x2 = float('inf')
        
        x1 = d[i - 1] + 1
        d.append(min(x1, x2, x3))
    
    k = n
    chain = [n]
    while k > 1:
        if k % 3 == 0 and d[k] == d[k // 3] + 1:
            k = k // 3
        elif k % 2 == 0 and d[k] == d[k // 2] + 1:
            k = k // 2
        else:
            k = k - 1
        chain.append(k)

    print(d[-1])
    print(*reversed(chain))


if __name__ == '__main__':
    calc()
 