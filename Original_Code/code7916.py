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

h1 = getIntInput()*60*60
m1 = getIntInput()*60
s1 = getIntInput()
h2 = getIntInput()*60*60
m2 = getIntInput()*60
s2 = getIntInput()
print(h2-h1+m2-m1+s2-s1) 