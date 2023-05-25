import sys

def isPrime(n):
        if n in [0, 1]:
                return False
        elif n==2:
                return True
        elif not n & 1:
                return False
        for i in range(3, int(n**0.5)+1, 2):
                if n%i==0:
                        return False
        return True

def primes():
        i = 2
        while True:
                if isPrime(i):
                        yield i
                i += 1

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
                return n #[0]
        else:
                return n

n = getIntInput()[0]
indices = getIntInput()
primeList = []
primeGenerator = primes()
while len(primeList) <= max(indices):
	primeList.append(next(primeGenerator))

result = []
for i in range(n):
    result.append(primeList[int(indices[i]-1)])
for i in range(n):
    sys.stdout.write(str(result[i]) + ' ') 