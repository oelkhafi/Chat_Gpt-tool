import sys
tree = []

for i in range(int(sys.stdin.readline())):
    tree.append(list(map(int, sys.stdin.readline().split())))

in_order_result = []
pre_order_result = []
post_order_result = []
def order(node):
    if node == -1:
        return
    pre_order_result.append(tree[node][0])
    order(tree[node][1])
    in_order_result.append(tree[node][0])
    order(tree[node][2])
    post_order_result.append(tree[node][0])

order(0)

print(*in_order_result)
print(*pre_order_result)
print(*post_order_result) 