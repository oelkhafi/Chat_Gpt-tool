def factorial(n):
    res = 1
    if n == 0 or n == 1:
        #print(1)
        return 1
    else:
        for i in range(1, n+1):
            res *= i
    #print(res)
    return res

def sf(n):
    res = 1
    for i in range(1, n+1):
        fac = factorial(i)
        res*= fac

    #print (res)
    return res
    
     