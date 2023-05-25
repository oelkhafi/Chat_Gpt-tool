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

n = getIntInput()
if n%2==0:
    print(n+2)
else:
    print(n+1) 