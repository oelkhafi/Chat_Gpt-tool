import sys

sys.stdin.readline()
mass = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

stek_max = [0]
max = 0

for i in range(len(mass) - m + 1):
    if len(stek_max) == 1:
        for j in range(m + i - 1, i - 1, -1):
            if stek_max[-1] < mass[j]:
                stek_max.append(mass[j])
            else:
                stek_max.append(stek_max[-1])
        max = 0
        print(stek_max[-1])
    else:
        if max < mass[i+m-1]:
            max = mass[i+m-1]
        stek_max.pop()
        if max > stek_max[-1]:
            print(max)
        else:
            print(stek_max[-1])



 