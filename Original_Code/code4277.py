clss = dict()
def isParent(chld, prnt):
    prnts = clss[chld]
    if chld == prnt or prnt in prnts:
        return True
    else:
        for p in prnts:
            if isParent(p, prnt):
                return True
        else:   return False

cldesc = [input().split(' : ') for i in range(int(input()))]
for cl in cldesc:
    clss[cl[0]] = [] if len(cl) == 1 else cl[1].split()

q = [input().split() for i in range(int(input()))]
for pred, cl in q:
    print('Yes' if isParent(cl, pred) else 'No')





 