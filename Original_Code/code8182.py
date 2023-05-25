def binary_search(sorted_ar, value):
    l = 0
    r = len(sorted_ar) - 1

    while l <= r:
        m = (l + r) // 2
        if sorted_ar[m] == value:
            # return m
            return m + 1
        elif sorted_ar[m] > value:
            r = m - 1
        else:
            l = m + 1

    return -1

ar = list(map(int, input().split()))[1:]
values = list(map(int, input().split()))[1:]

res = []
for value in values:
    res.append(binary_search(ar, value))

print(*res) 