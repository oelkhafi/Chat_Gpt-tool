def checkParent(class1,class2):
    if class1 in classes[class2] or class1 == class2: 
        return True
        
    else: 
        for classTemp in classes[class2]:
            if classTemp != 'object':
                if checkParent(class1,classTemp):
                    return True
        return False


classes = dict()

for i in range(int(input())):
    params = input().split()
    if len(params) > 1: classes[params[0]] = params[2:]
    else: classes[params[0]] = ['object']


for i in range(int(input())):
    class1,class2 = input().split()
    if checkParent(class1,class2): print('Yes')
    else: print('No') 