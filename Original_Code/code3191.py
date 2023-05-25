# put your python code here

a = [int(i)for i in input().split()]
summary = 0
n = 0

for j in a:
    n += 1
    if len(a) == 1:
        print(a[0])
        break
    try:
        summary = a[n - 2] + a[n]
        print(summary, end="" "")
    except IndexError:
        summary = a[n - 2]  + a[0]
        print(summary, end="" "")





 