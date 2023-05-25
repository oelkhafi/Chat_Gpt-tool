#!/usr/bin/env python3
# coding=utf-8


import string


def count_init_messages(sequence):
    def get_alpha(seq):
        nonlocal count

        if len(seq) == 0:
            count += 1
            return

        for i in range(1, len(seq) + 1):
            if seq[:i] not in alph_table:
                break
            else:
                get_alpha(seq[i:])

    alphabet = "" "" + string.ascii_uppercase
    alph_table = {str(n): alph for n, alph in zip(range(len(alphabet)), alphabet)}
    count = 0
    get_alpha(sequence)

    return count


def count_messages_dp(seq):
    cur_comb, prev_comb = 1, 1

    for i in range(1, len(seq)):
        cur_comb, prev_comb = cur_comb + (prev_comb if 9 < int(seq[i - 1:i + 1]) < 27 else 0), cur_comb

    return cur_comb


def main():
    sequence = input().rstrip()
    print(count_messages_dp(sequence))


if __name__ == ""__main__"":
    main()
 