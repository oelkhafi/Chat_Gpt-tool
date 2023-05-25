n = int(input())

for i in range(n//1000):
    print('M', end='')
n %= 1000

for i in range(n//900):
    print('CM', end='')
n %= 900

for i in range(n//500):
    print('D', end='')
n %= 500

for i in range(n//400):
    print('CD', end='')
n %= 400

for i in range(n//100):
    print('C', end='')
n %= 100

for i in range(n//90):
    print('XC', end='')
n %= 90

for i in range(n//50):
    print('L', end='')
n %= 50

for i in range(n//40):
    print('XL', end='')
n %= 40

for i in range(n//10):
    print('X', end='')
n %= 10

for i in range(n//9):
    print('IX', end='')
n %= 9

for i in range(n//5):
    print('V', end='')
n %= 5

for i in range(n//4):
    print('IV', end='')
n %= 4

for i in range(n//1):
    print('I', end='')
n %= 1 