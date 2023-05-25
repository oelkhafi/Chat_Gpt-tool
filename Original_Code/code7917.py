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

A = getIntInput()
B = getIntInput()
N = getIntInput()
print(' '.join([str(((A*100+B)*N)//100), str(((A*100+B)*N)%100)])) 