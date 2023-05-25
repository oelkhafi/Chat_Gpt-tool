# put your python code here
classExceptions = {}
exceptionList = []

def findParentException(excepts):
    if excepts in classExceptions.keys():
        exceptsParents = []
        if len(classExceptions[excepts]) != 0:
            parents = [i for i in classExceptions[excepts]]
            for i in parents:
                exceptsParents.append(i)
            for thisExcept in exceptsParents:
                if thisExcept in exceptionList:
                    return True
                    break
                else:
                    res = findParentException(thisExcept)
                    if res is True:
                        return True
    else:
        return
for n in range(int(input())):
    exceptions = [str(i) for i in input().split()]
    if exceptions[0] not in classExceptions:
        if (len(exceptions)) == 1:
            classExceptions[exceptions[0]] = set()
        else:
            classExceptions[exceptions[0]] = {exceptions[i] for i in range(2, len(exceptions))}
    else:
        for c in range(2, len(exceptions)):
            classExceptions[exceptions[0]].add(exceptions[c])
for q in range(int(input())):
    excepts = input()
    exceptionList.append(excepts)
    res = findParentException(excepts)
    if res is True:
        print(excepts) 