def isRisedOrRisedParent(exc):
    if exc in rised:
        return True
    parents = dexc.get(exc)
    for p in parents:
        if isRisedOrRisedParent(p):
            return True
    return False

import sys
infile = sys.stdin #  open('exxx.txt') # 

n = int(infile.readline().strip())
exc = [infile.readline().strip().split(' : ') for _ in range(n)]
dexc = dict((x[0], []) if len(x) == 1 else (x[0], x[1].split()) for x in exc)

m = int(infile.readline().strip())
errs = [infile.readline().strip() for _ in range(m)]
rised = set()

for err in errs:
    if isRisedOrRisedParent(err):
        print(err)
    rised.add(err)
 