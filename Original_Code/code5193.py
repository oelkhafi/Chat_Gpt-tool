num_dict = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

rom = input()
i = 0
res = 0
while i < len(rom):
    
    crnt = rom[i]
    if i + 1 < len(rom):
        nxt = rom[i+1]
    else:
        nxt = crnt
        
    if num_dict[crnt] < num_dict[nxt]:
        num = num_dict[crnt + nxt]
        i += 2
    else:
        num = num_dict[crnt]
        i += 1
    res += num

print(res)
 