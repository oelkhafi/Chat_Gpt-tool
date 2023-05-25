def chetnost_permutation(numbers):
    not_right_pairs_count = 0

    for index1, number1 in enumerate(numbers):
        for number2 in numbers[index1+1:]:
            if number1 > number2:
                not_right_pairs_count += 1

    return 1 if not_right_pairs_count % 2 == 0 else -1

def read_permutation(rows):
    return [int(number) for _ in range(rows) for number in input().split()]

def create_etalon_permutation_row(row_index, cols, adjust=0):
    max_index = row_index * cols
    min_index = (row_index - 1) * cols

    if row_index % 2 == 1:
        return [col for col in range(min_index + 1, max_index + 1 + adjust)]
    else:
        return [col for col in range(max_index + adjust, min_index, -1)]

def create_etalon_permutation(rows, cols):
    etalon = []

    # create first (rows - 1)
    for row in range(1, rows):
        etalon.extend(create_etalon_permutation_row(rows, cols))

    # create last row
    etalon.extend(create_etalon_permutation_row(rows, cols, -1))

    return etalon

def _main():
    rows, cols = map(int, input().split())

    etalon_permutation = create_etalon_permutation(rows, cols)
    curr_permutation = read_permutation(rows)

    if chetnost_permutation(curr_permutation) == chetnost_permutation(etalon_permutation):
        print('Бинго!')
    else:
        print('Не повезло...')

if __name__ == '__main__':
    _main()
 