from collections import OrderedDict


def to_roman(n):
    rom = OrderedDict([(1000, 'M'),
                      (900, 'CM'),
                      (500, 'D'),
                      (400, 'CD'),
                      (100, 'C'),
                      (90, 'XC'),
                      (50, 'L'),
                      (40, 'XL'),
                      (10, 'X'),
                      (9, 'IX'),
                      (5, 'V'),
                      (4, 'IV'),
                      (1, 'I')]
                     )
    roman = ''
    for k, v in rom.items():
        roman += n // k * v
        n %= k
    return roman


if __name__ == '__main__':
    print(to_roman(int(input())))
 