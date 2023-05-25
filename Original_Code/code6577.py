import sys
from collections import namedtuple

import sys
sys.setrecursionlimit(15000)

Node = namedtuple(""Node"", [""value"", ""left"", ""right""])
res = []

def in_order(tree, curr):
	global res
	if curr == -1:
		return None
	else:
		in_order(tree, tree[curr].left)
		res += [tree[curr].value]
		in_order(tree, tree[curr].right)


n = int(next(sys.stdin))
tree = [Node(*map(int, line.split())) for line in sys.stdin]
flag = True

if n: in_order(tree, 0)

for i in range(len(res) - 1):
	if res[i] > res[i+1]:
		flag = False
		break

print([""INCORRECT"", ""CORRECT""][flag]) 