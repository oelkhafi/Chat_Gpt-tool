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

g1 = getIntInput()
g2 = getIntInput()
g3 = getIntInput()
print(((g1//2)+(g1%2))+((g2//2)+(g2%2))+((g3//2)+(g3%2))) 