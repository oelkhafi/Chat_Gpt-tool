import array
import bisect


def nearest_to_num(sorted_arr, num):
    if num <= sorted_arr[0]:
        return 0
    elif num >= sorted_arr[-1]:
        return len(sorted_arr)-1
    else:
        index = bisect.bisect_left(sorted_arr, num)
        if ((num-sorted_arr[index-1]) <= (sorted_arr[index]-num)):
            return index-1
        else:
            return index


if __name__ == ""__main__"":
    num = int(input())
    sorted_arr = array.array(""i"", map(int, input().split()))
    num = int(input())
    array_of_int = array.array(""i"", map(int, input().split()))
    print(*[nearest_to_num(sorted_arr, num) for num in array_of_int])
 