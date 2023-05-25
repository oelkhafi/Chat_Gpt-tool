def gen_ticket_number(count, series, length=6):
    series_generator = gen_series(series)
    number_generator = gen_number(length)
    for series in series_generator:
        for number in number_generator:
            if not count:
                return
            yield ' '.join((number, series))
            count -= 1
        number_generator = gen_number(length)


def gen_series(series):
    series = series.upper()
    yield series
    while series != 'ZZ':
        first_sign, second_sign = map(ord, series)
        if second_sign == ord('Z'):
            series = chr(first_sign + 1) + 'A'
        else:
            series = chr(first_sign) + chr(second_sign + 1)
        yield series


def gen_number(length=6):
    for num in range(1, 10 ** length):
        yield str(num).zfill(length)
 