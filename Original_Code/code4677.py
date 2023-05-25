inheritance = {}


def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), inheritance[child]))


n = int(input())
for _ in range(n):
    line = [s.strip() for s in input().split()]
    inheritance[line[0]] = set() if len(line) == 1 else set(line[2:])

m = int(input())
catched = set()
for _ in range(m):
    current = input()
    for key in inheritance.keys():
        if key in catched and is_parent(current, key):
            print(current)
            break
    catched.add(current) 