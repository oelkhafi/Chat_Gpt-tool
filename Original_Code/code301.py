import sys


def find_index(a, b):
        lf = 1
        rt = n
        while lf <= rt:
            j = int((lf + rt) / 2)
            if a[j] == b:
                return j
            elif a[j] < b:
                lf = j + 1
            elif a[j] > b:
                rt = j - 1
        return -1


if __name__ == '__main__':
    a_array = list(map(int, sys.stdin.readline().split()))
    b_array = list(map(int, sys.stdin.readline().split()))
    n = a_array[0]
    k = b_array[0]
    sys.stdout.write(' '.join(map(str, [find_index(a_array, b_array[i]) for i in range(1, k + 1)])))
 