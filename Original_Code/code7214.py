def split_decode_series(string):
    import re

    patt = '\d*\D'
    for i in re.findall(patt, string):
        yield (1 if len(i) == 1 else int(i[:-1]), i[-1])


def decode_series(series):
    s = ''
    for i in series:
        s += i[0] * i[1]
    return s


def rle_decode(string):
    series = split_decode_series(string)
    return decode_series(series)


string = input()
print(rle_decode(string))
 