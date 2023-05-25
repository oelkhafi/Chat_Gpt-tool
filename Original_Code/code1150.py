from functools import reduce
from itertools import takewhile, tee
from math import sqrt

def inputGen():
    while True:
        yield input()
        
def mean(x, correct=False):
    res = reduce(lambda p, i: [p[0]+1, p[1]+i], x, [0, 0])
    if correct:
        res[0] -= 1
    return (res[1] / res[0]) if res[0] else 0

def std(x):
    gens = tee(x)
    mm = mean(gens[0])
    return sqrt(mean(map(lambda i: (i-mm)**2, gens[1]), True))


print(std(takewhile(lambda x: x != 0, map(int, inputGen()))))
 