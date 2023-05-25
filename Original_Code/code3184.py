# put your python code here
n1, n2 , n3 = int(input()), int(input()), int(input())
m = n1
l = n1
e = 0

if m < n2:
    m = n2
if m < n3:
    m = n3
if l > n2:
    l = n2
if l > n3:
    l = n3
e = (n1 + n2 + n3) - (m + l)

print(m)
print(l)
print(e)




 