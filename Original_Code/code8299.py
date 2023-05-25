def foo(dict1):
    for key in dict1.keys():
        for key2 in dict1.keys():
            if key in dict1[key2]:
                dict1[key2].extend(dict1[key])


ouf = set()
variation = set()
classes = {}
for i in range(int(input())):
    a = input().split()
    classes[a[0]] = []
    classes[a[0]].extend(a[2:])

foo(classes)

for i in range(int(input())):
    b = input()
    variation.add(b)
    for j in classes[b]:
        if j in variation and b not in ouf:
            print(b)
            ouf.add(b)
                              