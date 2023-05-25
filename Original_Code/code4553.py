number = int(input())
numbers = tuple([int(input()) for x in range(number)])
maxn, minn, nod = numbers[0], numbers[0], 1
for counter in numbers:
    if counter < minn:
        minn = counter
    if counter > maxn:
        maxn = counter
if maxn % minn == 0:
    nod = minn
else:
    for counter in range(2, round(minn ** 0.5) + 1):
        if minn % counter == maxn % counter == 0:
            nod = counter
print(nod)
simple = 'YES'
if nod == 1:
    simple = 'NO'
for counter in range(2, round(nod ** 0.5) + 1):
    if nod % counter == 0:
        simple = 'NO'
print(simple)
 