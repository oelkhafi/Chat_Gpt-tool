def parent(anc, heir, classes, past = set()): # anc - потенциальный предок, heir - потенциальный наследник
        if anc in classes[heir] or anc == heir: # условия Yes
            return True
        if classes[heir] == [] or heir in past: # условия поиска в ширину ([] как object)
            past.add(heir)
            return None
        if heir in classes[anc] : # условия No
            return False
        else:
            possible = classes[heir]
            if anc not in possible:
                for i in possible:
                    a = parent(anc, i, classes)
                    if a != None:
                        return a
classes = {}
n = int(input())
for i in range(n):
    potent = input()
    if ':' in potent:
        potent = potent.split()
        for i in potent[2:]:
            if i not in classes:
                classes[i] = []
            if potent[0] not in classes:
                classes[potent[0]] = [i]
            else:
                classes[potent[0]] += [i]
    else:
        classes[potent] = []       
n = int(input())
for i in range(n):
    anc, heir = input().split()
    print('Yes' if parent(anc, heir, classes) else 'No') 