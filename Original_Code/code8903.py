# put your python code here
a= int(input())
b= int(input())
c= int(input())
if a >=b:
    max=a
else:
    max=b
if c>=max:
    max=c
if a<=b:
    min=a
else:
    min=b
if c<=min:
    min=c
m=((a+b+c)-(min+max))
print(max)
print(min)
print(m)



 