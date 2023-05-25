def merge(a, b):
    tmp = []
    global k
    while a and b:
        if a[0] <= b[0]:
            tmp.append(a.pop(0))
        else:
            tmp.append(b.pop(0))
            k += len(a)
    tmp.extend(a or b)
    return tmp


def mergesort(lst):
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    return merge(mergesort(lst[: m]), mergesort(lst[m:]))
    

def main():
    n = int(input())
    queue = [int(i) for i in input().split()]
    mergesort(queue)
    print(k)


if __name__ == '__main__':
    k = 0
    main()
 