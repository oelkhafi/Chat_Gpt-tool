def merge(left, right):
    global k
    result = list()
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            k += len(left) - i
            j += 1
    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result

def mergesort(a):
    if len(a) > 1:
        middle = len(a) // 2
        left = a[:middle]
        right = a[middle:]
        return merge(mergesort(left), mergesort(right))
    else:
        return a

n, k = int(input()), 0
m = list(map(int, input().split()))
mergesort(m)
print(k)
 