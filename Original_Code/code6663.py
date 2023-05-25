k=[]

def mydeep(L1,k):
    for L in L1: 
        cicle(L,L1,k)
    return k
    
    
def cicle(L,L1,k) :   
    if type(L) is list:
        t=[]
        for elem in L: 
            cicle(elem,L,t) 
        k.append(t)
        
    else: 
        k.append(L)
    return k


        
    
L2= mydeep(L1,k) 