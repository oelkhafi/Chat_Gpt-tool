# put your python code here
def depth(parent, child):
    outData.update(set(inData[child]))
    for el in inData[child]:
        depth(parent, el)

n = int(input())
inData = dict()
for i in range(n):
    s = input().replace(':', ' ').split()
    if len(s) == 1: inData[s[0]] = []
    else: inData[s[0]] = s[1:]
# print(inData)
q = int(input())
for i in range(q):
    s = input().split()
    outData = set()
    outData.add(s[1])
    depth(s[0], s[1])
    # print(outData)
    if s[0] in outData: print('Yes')
    else: print('No') 