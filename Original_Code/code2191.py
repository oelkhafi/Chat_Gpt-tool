n = [int(i) for i in input().split(',')]
m = list(set(n))
m.sort()
maximum1 = []
maximum2 = []
for i in m:
    if (len(maximum1) == 0) or (len(maximum2) == 0):
        if len(maximum1) == 0:
            maximum1.append(i)
        elif len(maximum2) == 0:
            maximum2.append(i)
    elif abs(i) > abs(maximum1[0]):
        if abs(maximum1[0]) > abs(maximum2[0]):
            maximum2[0] = maximum1[0]
        maximum1[0] = i
    elif abs(i) < abs(maximum1[0]):
        if (abs(i) != abs(maximum1[0])) and (abs(i) > abs(maximum2[0])):
            maximum2[0] = i
if abs(maximum1[0]) > abs(maximum2[0]):
    maximum1[0], maximum2[0] = maximum2[0], maximum1[0]
print(*maximum1, *maximum2)
 