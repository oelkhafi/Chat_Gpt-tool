import sys
from collections import namedtuple  

def in_order(tree, curr):
	res = []
	if curr == -1:
		return []
	else:
		res += in_order(tree, tree[curr].left)
		res += [tree[curr].value]
		res += in_order(tree, tree[curr].right)
	return res

def pre_order(tree, curr):
	res = []
	if curr == -1:
		return []
	else:
		res += [tree[curr].value]
		res += pre_order(tree, tree[curr].left)		
		res += pre_order(tree, tree[curr].right)
	return res

def post_order(tree, curr):
	res = []
	if curr == -1:
		return []
	else:
		res += post_order(tree, tree[curr].left)
		res += post_order(tree, tree[curr].right)
		res += [tree[curr].value]
	return res

def main():
	Node = namedtuple(""Node"", [""value"", ""left"", ""right""])
	n = int(next(sys.stdin))
	tree = [Node(*map(int, line.split())) for line in sys.stdin]
	print(*in_order(tree, 0))
	print(*pre_order(tree, 0))
	print(*post_order(tree, 0))


if __name__ == ""__main__"":
	main()
	 