def chetnost_permutation(numbers):
    not_right_pairs_count = 0

    for index1, number1 in enumerate(numbers):
        for number2 in numbers[index1+1:]:
            if number1 > number2:
                not_right_pairs_count += 1

    return 1 if not_right_pairs_count % 2 == 0 else -1

def read_permutation():
    lines_count = 4
    
    return [int(number) for _ in range(lines_count) for number in input().split()]

def _main():
    etalon_permutation = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 15, 14, 13]

    curr_permutation = read_permutation()
    if chetnost_permutation(curr_permutation) == chetnost_permutation(etalon_permutation):
        print('Бинго!')
    else:
        print('Не повезло...')

if __name__ == '__main__':
    _main()
 