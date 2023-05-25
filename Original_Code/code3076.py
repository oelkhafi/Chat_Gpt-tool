def create_dict_from_pattern(values = {}):
    pattern = '''\
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000'''.split('\n')
    
    for line in pattern:
        key, value = map(str, line.split(' = '))
        values[int(value)] = key
    return values
    
    
def convert(dec, values, temp = []):
    for num in dec:
        if num == 0:
            continue
        elif num in values:
            temp.extend(values[num])
        else:
            if num in [4, 9, 40, 90, 400, 900]:
                bigger = min([x for x in sorted(list(values)) if x > num])
                dec = [bigger - num, bigger]
                convert(dec, values, temp)
            else:
                smaller = max([x for x in sorted(list(values)) if x < num])
                dec = [smaller, num - smaller]
                convert(dec, values, temp)
    return temp
        
        
def main():
    values = create_dict_from_pattern()
    s = input()
    if int(s) in values:
        print(values[int(s)])
    else:
        row = [1000, 100, 10, 1]
        s = s.zfill(4)
        dec = [row[i] * int(s[i]) for i in range(4)]

        roman = convert(dec, values)
        print(*roman, sep="""")
        return
    
    
main()  
 