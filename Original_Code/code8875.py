a = int(input()) 
b = int(input()) 
c = int(input()) 
if (a >= b) and (a >= c) and (c <= b <= a): 
   max_n = a 
   min_n = c 
   medium_n = b 
elif (a >= b) and (a >= c) and (b <= c <= a): 
   max_n = a 
   min_n = b 
   medium_n = c 
elif (b >= a) and (b >= c) and (a <= c <= b): 
   max_n = b 
   min_n = a 
   medium_n = c 
elif (b >= a) and (b >= c) and (c <= a <= b): 
   max_n = b 
   min_n = c 
   medium_n = a 
elif (c >= a) and (c >= b) and (a <= b <= c): 
   max_n = c 
   min_n = a 
   medium_n = b 
elif (c >= a) and (c >= b) and (b <= a <= c): 
   max_n = c 
   min_n = b 
   medium_n = a 
print(max_n) 
print(min_n) 
print(medium_n)




 