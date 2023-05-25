# put your python code here
def binary_search(_numbers, _item):
    left = 0
    right = len(_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if _numbers[mid] == _item:
            return mid + 1
        elif _numbers[mid] > _item:
            right = mid - 1
        elif _numbers[mid] < _item:
            left = mid + 1
    return -1


def main():
    numbers = list(map(int, input().split("" "")))[1:]
    search = list(map(int, input().split("" "")))[1:]
    result = [str(binary_search(numbers, item)) for item in search]
    print("" "".join(result))


if __name__ == ""__main__"":
    main()
 