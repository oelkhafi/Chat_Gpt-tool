def foo(dict1):
    for key in dict1.keys():
        for key2 in dict1.keys():
            if key in dict1[key2]:
                dict1[key2].extend(dict1[key])


classes = {}
for i in range(int(input())):
    a = input().split()
    classes[a[0]] = []
    for j in a:
        if j != a[0] and j != ':':
            classes[a[0]].append(j)
foo(classes)
for i in range(int(input())):
    b = input().split()
    if len(b) == 2:
        if b[0] in classes[b[1]] or b[0] == b[1]:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes' if b[0] in classes else 'No')


 