import sys


def merge(left, right):
    global counter
    merged_list = []
    len_l, len_r = len(left), len(right)
    begin_l, begin_r = 0, 0
    while len_l > 0 and len_r > 0:
        if left[begin_l] > right[begin_r]:
            merged_list.append(right[begin_r])
            len_r -= 1
            counter += len_l
            begin_r += 1
        else:
            merged_list.append(left[begin_l])
            len_l -= 1
            begin_l += 1
    if len_l > 0:
        merged_list += left[begin_l:]
    elif len_r > 0:
        merged_list += right[begin_r:]
    return merged_list


counter = 0
n = int(input())
A = [[int(i)] for i in sys.stdin.readline().split()]
k = 0
begin = 0

while n > 1:
    if k == 0 and n > 2:
        if n % 2 != 0:
            A.append(merge(A.pop(-2), A.pop(-1)))
            n -= 1
        k = n // 2
    A.append(merge(A[begin], A[begin+1]))
    n -= 1
    k -= 1
    begin += 2
print(counter) 