a = int(input())
c = 1
max_value = 1
min_value = 300
while c <= a:
    c+=1
    b = round(float(input()))
    if b > max_value:
        max_value = b
    if b < min_value:
        min_value = b    
print(max_value)
if min_value < 30:
    print(""YES"")
else:
    print(""NO"")




 