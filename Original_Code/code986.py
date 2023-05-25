import sys
def add(hash, v):
    if v in hash: print('FAIL')
    else:
        hash.update({v})
        print('OK')

def delete(hash, v):
    if v not in hash: print('FAIL')
    else:
        hash.difference_update({v})
        print('OK')

def isit(hash,v):
    if v in hash: print('OK')
    else: print('FAIL')

hash = set()
operations = {'+':add, '-':delete, '?':isit}
for line in sys.stdin:
    c, v = line.strip().split()
    if c == '+': add(hash, v)
    elif c == '-': delete(hash, v)
    else: isit(hash, v) 