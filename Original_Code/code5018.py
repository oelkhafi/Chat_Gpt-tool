def kaprekar_step(n):
    digits = sorted(list(str(n)))

    min_number_str = ''.join(digits)

    return int(min_number_str[::-1]) - int(min_number_str)


def kaprekar_check(n):
    n_str = str(n)
    digits = list(n_str)
    digits_count = len(digits)
    checking_dict = {3: 100, 4: 1000, 6: 100000}

    return (digits_count in checking_dict) and (n not in checking_dict.values()) and len(set(n_str)) > 1


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(n))
    else:
        prev_number = curr_number = n
        prev_numbers = set()

        while True:
            print(prev_number)

            curr_number = kaprekar_step(prev_number)
            if prev_number == curr_number:
                break
            elif curr_number in prev_numbers:
                print(""Следующее число - {}, кажется процесс зациклился..."".format(curr_number))
                break

            prev_number = curr_number
            prev_numbers.add(prev_number)

 