s = input().split()
u = []
ic = 0
ic1 = 0
for c in s:
    for c1 in s:
        if (c1 == c and ic != ic1):
            flag1 = False
            for au in u:
                if au == c1:
                    flag1 = True
                    break
            if not flag1:
                u.append(c1)
            else:
                flag1 = False
            break
        ic1 += 1
    ic1 = 0
    ic += 1
for e in u:
    print(e, end=' ')
 