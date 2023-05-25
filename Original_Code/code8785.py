# put your python code here
import random


def quick_sort_3(_array, left, right):
    if left >= right:
        return

    lt = left
    gt = right

    pivot = _array[random.randint(left, right)]

    i = left
    while i <= gt:
        if _array[i] < pivot:
            _array[lt], _array[i] = _array[i], _array[lt]
            lt += 1
            i += 1
        elif _array[i] > pivot:
            _array[gt], _array[i] = _array[i], _array[gt]
            gt -= 1
        else:
            i += 1

    quick_sort_3(_array, left, lt - 1)
    quick_sort_3(_array, gt + 1, right)


def binary_search(_array, point, n):
    left, right = 0, len(_array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if _array[m] <= point - n:
            left = m + 1
        elif _array[m] > point - n:
            right = m - 1
    return left


def main():
    n, m = map(int, input().split())
    starts = []
    ends = []
    for i in range(n):
        segments = list(map(int, input().split("" "")))
        starts.append(segments[0])
        ends.append(segments[1])
    points = list(map(int, input().split("" "")))
    quick_sort_3(starts, 0, len(starts) - 1)
    quick_sort_3(ends, 0, len(starts) - 1)
    result = []
    for point in points:
        count1 = binary_search(starts, point, 0)
        count2 = binary_search(ends, point, 1)
        result.append(count1 - count2)
    print(*result)


if __name__ == ""__main__"":
    main()
 