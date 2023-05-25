import sys

def getIntInput():
        #print(""Please insert (an) integer value(s):"")
        while True:
                try:
                        n = list(map(int, sys.stdin.readline().split()))
                        break
                except ValueError as ex:
                        print(""Error with data type. Please insert an integer value:"")
                        pass
        #print(""Thank you!"")
        if len(n) == 1:
                return n[0]
        else:
                return n
                
def getMaxPairProduct(seq):
    n1 = max(seq)
    seq.remove(n1)    
    return n1*max(seq)

n = getIntInput()
seq = getIntInput()
print(getMaxPairProduct(seq)) 