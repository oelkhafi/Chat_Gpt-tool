def kaprekar_loop(n):   
    def kaprekar_check(n):
        if len(numerics(n)) in [3,4,6] and len(set(numerics(n)))!=1 and n not in [100, 1000, 100000]:
            return(True)
        return(False) 

    def numerics(n):
        n=list(map(int, str(n)))
        return(n)
    
    def kaprekar_step(L):
        LSI=int(''.join(str(x) for x in sorted(L)))
        LSRI=int(''.join(str(x) for x in sorted(L, reverse=True)))
        return(LSRI-LSI)    
         
    if kaprekar_check(n)==False:
        print('Ошибка! На вход подано число ' + str(n) + ', не удовлетворяющее условиям процесса Капрекара')    
    else:
        se=[]
        print(n)
        while n not in [495, 6174, 549945, 631764]:
            n=kaprekar_step(numerics(n))
            if (len(numerics(n))==6) and (n in se):
                print('Следующее число - ' + str(n) + ', кажется процесс зациклился...')
                break
            print(n)
            se.append(n) 