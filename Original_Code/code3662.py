import json

def checkParent(class1, class2):
    if class1 in classes[class2] or class1 == class2:
        return True

    else:
        for classTemp in classes[class2]:
            if checkParent(class1, classTemp):
                return True
        return False


classes = dict()
classes_p = dict()

data = json.loads(input())
for cl in data:
    classes[cl['name']] = cl['parents']
    classes_p[cl['name']] = 0

for cl1 in classes_p:
    for cl2 in classes_p:
        if checkParent(cl1, cl2): classes_p[cl1] += 1

for cl in sorted(classes_p):
    print(cl, ':', classes_p[cl]) 