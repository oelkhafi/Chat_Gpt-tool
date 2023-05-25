n = int(input())
n_max = n
n_min = n
rem = n

n = int(input())
if n > n_max:
    n_max = n
elif n < n_min:
    n_min = n
    
n = int(input())
if n >= n_max:
    rem = n_max
    n_max = n    
elif n <= n_min:
    rem = n_min
    n_min = n
else:
    rem = n
    
print(n_max)
print(n_min)
print(rem)
 