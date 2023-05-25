# put your python code here
def binary_search(_array, item):
    first = 0
    last = len(_array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if _array[midpoint] == item:
            return midpoint
        else:
            if item < _array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1


def get_count(_array):
    count = 0
    b_list = list(_array)
    b_list.sort()
    for i in range(len(_array)):
        j = binary_search(b_list, _array[i])
        while b_list[j] == b_list[j - 1]:
            if j < 1:
                break
            j -= 1

        count += j
        b_list.pop(j)

    return count


def main():
    n = int(input())
    a_list = list(map(int, input().split("" "")))
    print(get_count(a_list))


if __name__ == ""__main__"":
    main()
 