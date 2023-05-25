count = 0


def merge_sort(ar):
    if len(ar) < 2:
        return ar
    m = len(ar) // 2
    return merge(merge_sort(ar[:m]), merge_sort(ar[m:]))


def merge(l, r):
    global count
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            count += len(l) - i
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result

input()
ar = tuple(map(int, input().split()))
merge_sort(ar)
print(count) 