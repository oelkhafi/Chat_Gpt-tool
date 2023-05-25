n = int(input())
num1 = int(input())
max = num1
min = num1
for i in range(n-1):
    a = int(input())
    if a >= max:
        max = a    
    elif a < min:
        min = a
while min != 0:
    max, min = min, max % min
    nod = max
answer = ""YES""    
for delit in range(2, int(nod ** 0.5) + 2):
    if nod % delit == 0 and nod != delit:
        answer = ""NO""
if nod == 1:
    answer = ""NO""
print(nod)
print(answer)
    





 