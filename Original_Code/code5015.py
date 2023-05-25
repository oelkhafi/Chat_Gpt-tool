def kaprekar_step_str(n):
    digits = [item for item in str(n)]
    digits.sort()
    min_number = int(''.join(digits))
    max_number = int(''.join(digits[::-1]))

    return max_number - min_number


def kaprekar_loop(n):
    if not (1000 <= n <= 9999):
        raise ValueError('Only 4 digits integer is supported')

    prev_number = n
    while True:
        print(prev_number)
        curr_number = kaprekar_step_str(prev_number)
        if prev_number == curr_number:
            break
        prev_number = curr_number

 