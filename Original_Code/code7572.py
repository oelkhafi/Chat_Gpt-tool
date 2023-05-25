def dfactorial(n):
    if n == 0 or n==1:
        return 1
    
    res1=1
    
    if n%2==0:
        i=2
        while i<=n:
            res1*=i
            i+=2
        return res1
    
    else:
        i=1
        while i<=n:
            res1*=i
            i+=2
        return res1
    


 