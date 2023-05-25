import sys
from collections import namedtuple

Node = namedtuple(""Node"", [""value"", ""left"", ""right""])
Order = namedtuple(""Order"", [""pre"", ""middle"", ""post""])

def walk(tree, curr, order):
	if curr != -1:
		order.pre.append(tree[curr].value)
		walk(tree, tree[curr].left, order)
		order.middle.append(tree[curr].value)
		walk(tree, tree[curr].right, order)
		order.post.append(tree[curr].value)


n = int(next(sys.stdin))
tree = [Node(*map(int, line.split())) for line in sys.stdin]
order = Order([], [], [])
walk(tree, 0, order)
print(*order.middle)
print(*order.pre)
print(*order.post) 