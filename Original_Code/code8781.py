# put your python code here
def huffman_decode(encoded, code):
    result = """"
    string = """"
    for i in encoded:
        string += i
        for j in code:
            if code.get(j) == string:
                result += j
                string = """"
                break
    return result


def main():
    letters, size = map(int, input().split("" ""))
    code = {}
    for i in range(0, letters):
        l, c = map(str, input().split("": ""))
        code[l] = c
    encoded = input()
    print(huffman_decode(encoded, code))


if __name__ == ""__main__"":
    main()
 