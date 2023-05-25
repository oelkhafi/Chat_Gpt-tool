# put your python code here
def max_sub_array(array):
    cur_sum = max_sum = -INF
    for item in array:
        cur_sum = max(item, cur_sum + item)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def max_sub_matrix(matrix):
    max_sum = -INF
    for row in range(len(matrix)):
        partial_sum = [0] * len(matrix[0])
        for row_end in range(row, len(matrix)):
            partial_sum = [x + y for x, y in zip(partial_sum, matrix[row_end])]

            max_sum = max(max_sum, max_sub_array(partial_sum))

    return max_sum


INF = 101
rows, _ = map(int, input().split())
print(max_sub_matrix([tuple(map(int, input().split())) for _ in range(rows)])) 