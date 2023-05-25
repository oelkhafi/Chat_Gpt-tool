a = [int(i) for i in input().split()]
s = sorted(a)
j = len(s)
x = []

for i in range(j):
    if j == 1:
        break
    if s[0] == s[-1]:
        print(s[i])
        break
    if s[i] == s[(i + 1) % j]:
        i += 1
    elif s[i] != s[(i - 1) % j]:
        i += 1
        continue
    else:
        x.append(s[i])

for k in range(len(x)):
    print(x[k], end=' ')
 