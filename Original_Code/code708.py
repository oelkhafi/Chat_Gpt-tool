def calculator(num):
    t = [None, [0, 0]]
    for i in range(2, num + 1):
        ops = [[t[i - 1][0] + 1, i - 1]]
        if i % 2 == 0:
            ops.append([t[i // 2][0] + 1, i // 2])
        if i % 3 == 0:
            ops.append([t[i // 3][0] + 1, i // 3])
        t.append(min(ops))
    return t

num = int(input())
res = calculator(num)
print(res[num][0])
i = num
steps = []
while i > 0:
    steps.append(i)
    i = res[i][1]
steps.reverse()
print(*steps) 