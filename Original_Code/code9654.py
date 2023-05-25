first_str = input()
second_str = input()
uncoded_str = input()
coded_str = input()


def coding(transform_str, *code_and_uncode, key = 'code'):
    code_dict = code_and_uncode[0]
    uncode_dict = code_and_uncode[1]
    if key == 'code':
        coded = ''
        for ch in transform_str:
            coded += code_dict[ch]
        return coded
    if key == 'uncode':
        uncoded = ''
        for ch in transform_str:
            uncoded += uncode_dict[ch]
        return uncoded

keys = [x for x in first_str]
vals = [x for x in second_str]
dic_coded = dict(zip(keys, vals))
dic_uncoded = dict(zip(vals, keys))
coded = coding(uncoded_str, dic_coded, dic_uncoded)
uncoded = coding(coded_str, dic_coded, dic_uncoded, key='uncode')
print(coded)
print(uncoded) 