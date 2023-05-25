card = [i for i in input().split()]
ans = list()
for i in range(len(card)):
    s = card[i]
    for j in range(len(card)):
        if j == i:
            continue
        else:
            s += card[j]
    if s not in ans and int(s) > 99:
        ans.append(s)
    s = card[i]
    for j in reversed(range(len(card))):
        if j == i:
            continue
        else:
            s += card[j]
    if s not in ans and int(s) > 99:
        ans.append(s)
for i in sorted(ans):
    print(i) 