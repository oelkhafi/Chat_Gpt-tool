# put your python code here
list = [int(i) for i in input().split()]
i = 0
j = 0
len = len(list)
if (len == 1):
    print(list[0])
else:
    while len > i:
        if i == 0:
            print(list[-1] + list[1], end=' ')
            i += 1
            continue
        elif i == len - 1:
            print(list[-2] + list[0], end=' ')
            i += 1
            break
        else:
            print(list[i - 1] + list[i + 1], end=' ')
            i += 1
 