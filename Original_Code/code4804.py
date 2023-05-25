from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(1000000)

def make_tree(line):

    tree = defaultdict(list)

    for i, node in enumerate(line.split(' ')):
        node = int(node)
        if node == -1:
            tree['root'] = i
        else:
            tree[node].append(i)
    return tree


def tree_height(tree):

    height = 0

    if 'root' not in tree:
        return height

    def recursive_search(tree, root: int, height: int):
        height += 1
        heights = [height]
        for node in tree[root]:
            heights.append(max(recursive_search(tree, node, height), height))
        return max(heights)

    return recursive_search(tree, tree['root'], height)


if __name__ == '__main__':

    n = input()
    line = input()
    tree = make_tree(line)
    height = tree_height(tree)
    print(height)
 