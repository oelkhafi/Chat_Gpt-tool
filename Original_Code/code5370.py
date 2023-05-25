#!/usr/bin/env python3
# coding=utf-8


def various_sum(seq):
    ds = set([0])
    cur_sums = set()

    for elem in seq:
        for s in ds:
            cur_sums.add(elem + s)
        ds.update(cur_sums)

    return len(ds)


def main():
    N = int(input())
    seq = tuple(map(int, input().split()))

    print(various_sum(seq))


if __name__ == ""__main__"":
    main()
 