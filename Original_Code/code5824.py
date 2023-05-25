def knapsack(volume, objects):
    max_value = 0
    for obj in objects:
        obj[0] = obj[0] / obj[1]
    objects.sort(reverse=True)
    for obj in objects:
        if obj[1] <= volume:
            max_value += obj[0] * obj[1]
            volume -= obj[1]
            if volume <= 0:
                break
        else:
            max_value += obj[0] * volume
            break
    return max_value


things = []
n, W = [int(i) for i in input().split(' ')]
for i in range(n):
    things.append([int(j) for j in input().split(' ')])

print('{0:.3f}'.format(knapsack(W, things)))
 