num_dict = {
    1000: 'M', 
    900: 'CM', 
    500: 'D', 
    400: 'CD', 
    100: 'C', 
    90: 'XC', 
    50: 'L', 
    40: 'XL', 
    10: 'X', 
    9: 'IX', 
    5: 'V', 
    4: 'IV', 
    1: 'I'
}

num = int(input())
res = ''
for i in num_dict:
    if num % i < num:
        res += str(num_dict[i]) * (num // i)
        num = num % i
print(res)
 