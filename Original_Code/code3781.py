inp = int(input())
h = {1: [n for n in range(inp, 0, -1)], 2: [], 3: []}

def sw(ra, rb):
    if not len(h[ra]):
        h[ra].append(h[rb].pop(-1))
        print(str(rb) + ' - ' + str(ra))
    elif not len(h[rb]):
        h[rb].append(h[ra].pop(-1))
        print(str(ra) + ' - ' + str(rb))
    elif h[ra][-1] > h[rb][-1]:
        h[ra].append(h[rb].pop(-1))
        print(str(rb) + ' - ' + str(ra))
    else:
        h[rb].append(h[ra].pop(-1))
        print(str(ra) + ' - ' + str(rb))
    if len(h[3]) == inp:
        exit()

while True:
    if inp % 2:
        sw(1, 3)
        sw(1, 2)
        sw(2, 3)
    else:
        sw(1, 2)
        sw(1, 3)
        sw(2, 3) 