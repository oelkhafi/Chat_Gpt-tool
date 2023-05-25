# put your python code here
import sys

sys.setrecursionlimit(100000)

def height(tr, r):
    h = 1
    if r in tr:
        for c in tr[r]:
            h = max(h, 1 + height(tr,c))
    return h


tree = dict()
input()
numbers = [int(i) for i in input().split()]
for i in range(len(numbers)):
    if numbers[i] in tree:
        tree[numbers[i]].append(i)
    else:
        tree[numbers[i]] = [i]

#print(tree)

print(height(tree, -1) - 1)



 