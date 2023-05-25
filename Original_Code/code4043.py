dna = input()
result = ''
char = dna[0]
index = 0
start = 0
end = 0

for i in dna:
    if i == char:
         end+=1
    else:
        s = dna[start:end]
        result += '{}{}'.format(char,len(s))
        char = i
        end = 1
    if index+1 == len(dna):
        s = dna[start:end]
        result += '{}{}'.format(char,len(s))
        
    index+=1
    
print(result)

 