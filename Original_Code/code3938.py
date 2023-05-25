def merge_sort(seq):
    if len(seq) < 2:
        return seq
    res = []
    med = len(seq) // 2
    left = merge_sort(seq[:med])
    right = merge_sort(seq[med:])
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(right[0])
            right.pop(0)
        else:
            res.append(left[0])
            left.pop(0)
    res += left
    res += right
    return res


input()
seq = list(map(int, input().split()))
input()
print(*merge_sort(seq))
 