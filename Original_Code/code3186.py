# put your python code here

a, b = int(input()), int(input())
d = 0
i = 0
j = 0
result1 = 0
result2 = 1
while True:
    i += 1
    j += 1
    if result1 == result2:
        d = result1
        print(d)
        break
    if i % a == 0:
        result1 = i
    if j % b == 0:
        result2 = j


 