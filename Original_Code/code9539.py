# put your python code here
a = [int(i) for i in input().split()]
lengthspisik = len(a) - 1
result=[]
z = -1
x = 1
if lengthspisik == 0:
    print(a[0])
else:
    for col in a:
        print(a[z] + a[x], end= ' ')
        z += 1
        x += 1
        if x > lengthspisik:
            x = x - x
    

     
    
     
     






 