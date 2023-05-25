objs = {}
uses = []
def test (parent, child):
    return parent == child or any(map(lambda select: test(parent, select), objs[child]))
for i in range(int(input())):
    line = input().split()
    objs [line[0]] = line[2:]
for i in range(int(input())):
    line = input()
    new = True;
    for e in uses:
        if test (e, line):
            print (line)
            new = False
            break
    if new:
        uses += [line]




 