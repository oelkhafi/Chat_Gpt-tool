def L2n(n):
    return calc(n)**2 - 2 * (-1)**n

def L3n(n):
    return calc(n)**3 - 3 * (-1)**n * calc(n)

def L5n(n):
    return calc(n)**5 - 5 * (-1)**n * calc(n)**3 + 5 * calc(n)
    
def calc(n):
    L = [2,1]
    for i in range(n-1):
        L[0], L[1] = L[1], L[0] + L[1]
    return L[1]

def super_L(n):
    list_del = [ 5, 3, 2]
    for i in list_del:
        if n%i == 0:
            if i == 5:
                return L5n(int(n/i))
            elif i == 3:
                return L3n(int(n/i))
            elif i == 2:
                return L2n(int(n/i))
            break
        else:
            return(calc(n)) 