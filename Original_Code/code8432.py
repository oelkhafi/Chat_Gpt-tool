genome = str(input())
line = ''
if len(genome) == 1:
    print(genome + '1')
else:
    i = 0
    while i < len(genome) - 1:  # len(genome) - 1 — это последний сим.
        if genome[i] == genome[i + 1]:
            counter = 1
            fragment = genome[i]
            while genome[i] == genome[i + 1]:
                counter += 1
                i += 1
                if i == len(genome) - 1:
                    break    
            line += fragment + str(counter)
            continue
            if i == len(genome) - 1:
                break
        if i != len(genome) - 1:
            if genome[i] != genome[i+1] and genome[i] != genome[i-1]:
                line += genome[i] + '1'
                i += 1
                if i == len(genome) - 1:
                    continue    
            if genome[i] != genome[i+1] and genome[i] == genome[i-1]:
                i += 1
                continue
    if i == len(genome) - 1:
        if genome[i] != genome[i-1]:
            line += genome[i] + '1'
        if genome[i] == genome[i-1]:
            line = line
print(line) 