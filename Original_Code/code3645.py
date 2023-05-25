def findParent(pretendent, child):
    if pretendent in exep[child]: return True
    else:
        for ch in exep[child]:
            if len(exep[ch]) != 0:
                if findParent(pretendent, ch):
                    return True
        return False
    
exep = dict()
answer = []
test = []
for i in range(int(input())):
    params = input().split()
    if len(params) > 1: exep[params[0]] = params[2:]
    else: exep[params[0]] = []

for i in range(int(input())):
    test+=[input()]

for i in range(1,len(test)):
    for j in range(0,i):
        if test[j] not in answer:
            if findParent(test[j], test[i]):
                answer += [test[i]]
if len(answer) > 0:
    print(answer[0])
    for i in range(1,len(answer)):
        if answer[i] != answer[i-1]:
            print(answer[i]) 