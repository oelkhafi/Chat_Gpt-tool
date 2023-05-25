def convert(n, base_to=10, base_from=10):
    string = ""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ""
    n = str(n)
    k = len(n)-1
    n10 = 0
    # conv n to base10:
    while k>=0:
        n10+=(string.index(n[k]))*base_from**(len(n)-1-k)
        k=k-1
    #return n10
    n_out=""""
    while n10 >= 1:
        n_out=str(n_out)+string[int(n10%base_to)]
        n10/=base_to
      
    return n_out[-1::-1]
    
    


 