# put your python code here
def huffman_encode(string):
    _dict, result = {}, {}

    for i in string:
        if i in _dict:
            _dict[i] += 1
        else:
            _dict[i] = 1

    if len(_dict) == 1:
        result[string[0]] = ""0""
    else:
        while len(_dict) > 1:
            left_key = min(_dict, key=_dict.get)
            left = _dict[left_key]
            del _dict[left_key]

            right_key = min(_dict, key=_dict.get)
            right = _dict[right_key]
            del _dict[right_key]

            for x in left_key:
                if x in result:
                    result[x] = '0' + result[x]
                else:
                    result[left_key] = '0'
            for y in right_key:
                if y in result:
                    result[y] = '1' + result[y]
                else:
                    result[right_key] = '1'

            _dict[left_key + right_key] = left + right
    return result


def main():
    string = input()
    code = huffman_encode(string)
    encoded = """".join(code[ch] for ch in string)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(""{}: {}"".format(ch, code[ch]))
    print(encoded)


if __name__ == ""__main__"":
    main()
 