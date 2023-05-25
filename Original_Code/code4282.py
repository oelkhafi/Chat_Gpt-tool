import json

chlds, prnts = dict(), dict()

def visit_prnts(chi, prn):
    chlds[prn].add(chi)
    if prnts.get(prn):
        # заходим к родителям родителя
        for x in prnts[prn]:
            visit_prnts(chi, x)

classes = json.loads(input())

for klass in classes:
    kl_name = klass['name']
    prnts[kl_name] = klass['parents']
    chlds[kl_name] = set()

for klass in classes:
    kl_name = klass['name']
    # начинаем обход с себя, т.к. сам себе тоже родитель
    visit_prnts(kl_name, kl_name)

print(*[cl+' : '+str(len(chlds)) for cl, chlds in sorted(chlds.items())], sep='\n')
 