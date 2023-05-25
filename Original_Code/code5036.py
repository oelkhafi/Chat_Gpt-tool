from collections import deque

def add_node(tree, parent, child):
    tree[child] = parent

def node_not_exists(tree, key, restriction):
    return key not in tree and key <= restriction

def get_operations_iter(number):
    tree = {0: 0, 1: 0}

    queue = deque([1])
    while number not in tree:
        parent = queue.popleft()

        child3 = parent * 3
        if node_not_exists(tree, child3, number):
            add_node(tree, parent, child3)
            queue.append(child3)

        child2 = parent * 2
        if node_not_exists(tree, child2, number):
            add_node(tree, parent, child2)
            queue.append(child2)

        child1 = parent + 1
        if node_not_exists(tree, child1, number):
            add_node(tree, parent, child1)
            queue.append(child1)

    # create sequence from tree
    sequence = []
    # start sequence from the end
    parent = number
    while parent > 0:
        sequence.append(parent)
        parent = tree[parent]

    # reverse sequence
    return len(sequence) - 1, sequence[::-1]

def main():
    number = int(input())
    k, numbers = get_operations_iter(number)
    print(k)
    print(*numbers, sep=' ')

if __name__ == '__main__':
    main() 