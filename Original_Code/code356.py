# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(11):
    if 0 < i < a or i > b:
        continue
    elif i == 0:
        p = i + 1
    else:
        p = i
    for j in range(11):
        if 0 < j < c or j > d:
            continue
        elif j == 0:
            q = j + 1
        else:
            q = j
        if i == 0 and j == 0:
            s = ' '
        else:
            s = p * q
        print(s, end='\t')
    print()
 