# put your python code here
a, b, c = int(input()), int(input()), int(input())
max = a
if b > max :
    max = b
    if c > max :
        max = c
else:
    if c > max :
        max = c
print(max)        

da, db, dc = max-a, max-b, max-c
min = da
if db > min :
    min = db
    if dc > min :
        min = dc
else:
    if dc > min :
        min = dc
        
print(max-min)
print(a+b+c-max-(max-min)) 