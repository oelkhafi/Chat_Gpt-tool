# put your python code here

num = [int(i) for i in input().split()]
num2 = num.copy()
for j in num2:
    if len(num) == 1:
        break
    elif num.count(j) > 1:
        print(j, end="" "")
        while j in num:
            num.remove(j)         
           
        
        
        

 





 