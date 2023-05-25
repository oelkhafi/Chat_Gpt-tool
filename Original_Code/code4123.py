DNA = str(input())
con = 0
DNA_2 = ''
x = 0
if len(DNA) < 2:
    print (DNA, len(DNA), sep='')
else:
    for i in DNA[x:]:
        con = 0
        DNA_1 = 0
        for j in DNA[x:]:
            if j == i:
                con += 1
                x += 1
            else:
                break
        if con != 0:
            con = str(con)
            DNA_1 = i+con
            con = int(con)
            DNA_2 += DNA_1
print(DNA_2) 