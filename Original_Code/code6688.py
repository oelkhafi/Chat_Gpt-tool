M=[]

def kaprekar_loop(n):
    if not kaprekar_check(n): print (""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(str(n)))
    else:
        print (n)
        new = kaprekar_step(numerics(n))
        M.append(n)
        if new!=n:
            if new in M: 
                print(""Следующее число - {}, кажется процесс зациклился..."".format(str(new)))
            else: kaprekar_loop(new)
        pass



def numerics(n):
    return [int(i) for i in str(n)]
    #your code

def kaprekar_check(n):
    k = str(n)
    if len(k)!=3 and len(k)!=4 and len(k)!=6 : return False
    elif n==100 or n==1000 or n==100000 : return False
    elif len(set(numerics(n)))==1: return False
    else: return True
    #your code   
    
def kaprekar_step(L):
    a = """"
    b = """"
    for i in sorted(L):
        a=a+str(i)
        b=str(i)+b
    return int(b)-int(a)

 