num_rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
rom = input()
num_arab = 0
i = 0
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
while i < len(rom):

    if i == len(rom)-1:
        num_arab += num_rom[rom[i]]
        break

    elif num_rom[rom[i]] < num_rom[rom[i+1]]:
        num_arab += num_rom[rom[i+1]] - num_rom[rom[i]]
        i += 2

    elif num_rom[rom[i]] > num_rom[rom[i+1]]:
        num_arab += num_rom[rom[i]]
        i += 1

    else:
        num_arab += num_rom[rom[i]]
        i += 1

print(num_arab)
 