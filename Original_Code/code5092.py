from collections import defaultdict
from sys import setrecursionlimit


def main():
    setrecursionlimit(10 ** 5)
    tree = defaultdict(list)
    count = int(input())
    data = [int(i) for i in input().split()]
    for i in range(count):
        tree[data[i]].append(i)
    print(height_tree(tree))


def height_tree(tree, node=-1):
    height = 0
    for i in tree[node]:
        height = max(height, 1 + height_tree(tree, i))
    return height


if __name__ == ""__main__"":
    main()
 