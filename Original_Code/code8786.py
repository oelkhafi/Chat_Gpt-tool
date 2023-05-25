# put your python code here
def count_sort(array, num):
    count = [0]*11
    for i in range(0, num):
        count[array[i]] += 1
    ind = 0
    while ind < len(count) - 1:
        count[ind + 1] += count[ind]
        ind += 1

    sorted_array = [0] * len(array)
    for j in range(len(array) - 1, -1, -1):
        sorted_array[count[array[j]] - 1] = array[j]
        count[array[j]] -= 1
    return sorted_array


def main():
    n = int(input())
    numbers = list(map(int, input().split("" "")))
    for y in count_sort(numbers, n):
        print(y, end=' ')


if __name__ == ""__main__"":
    main()
 