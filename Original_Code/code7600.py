import sys

def numerics(n):
    L = []
    n = str(n)
    for i in range(4):
        L.append(n[i])

    for j in range(4):
        L[j] = int(L[j])

    kaprekar_step(L)

def kaprekar_step(L):
    max = sorted(L)
    min = sorted(L, reverse=True)

    maxS = str(max[0])+str(max[1])+str(max[2])+str(max[3])
    minI=int(maxS)
    #print(maxS)
    minS = str(min[0])+str(min[1])+str(min[2])+str(min[3])
    maxI=int(minS)
    #print(minS)
    n = maxI - minI

    kaprekar_loop(n)

def kaprekar_loop(n):
    while True:
        print (n)
        #return(n)
        if n==6174:
            #return n
            sys.exit()
        else:
            numerics(n)

#n = 6174
#numerics(n) 