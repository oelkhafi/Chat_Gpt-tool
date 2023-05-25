import sys
sys.setrecursionlimit(20000)
tree = []
for i in range(int(sys.stdin.readline())):
    tree.append(list(map(int, sys.stdin.readline().split())))

in_order_result = []

result = ['CORRECT']

def LeftChild(node):
    if tree[node][1] == -1:
        return -1
    else:
        return tree[tree[node][1]][0]

def order(node):
    if node == -1:
        return
    order(tree[node][1])

    if len(in_order_result) > 0 and tree[node][0] < in_order_result[-1] or tree[node][0] == LeftChild(node):
        result[0] = 'INCORRECT'
        return
    else:
        in_order_result.append(tree[node][0])

    order(tree[node][2])

if len(tree) > 1:
    order(0)
print(result[0])

 