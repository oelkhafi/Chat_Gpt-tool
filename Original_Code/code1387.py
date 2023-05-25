def code_decode(a, cypher, code_from, code_to):
    result = ''
    code = dict()

    if cypher:
        code_from, code_to = code_to, code_from

    for i in range(len(code_from)):
        code[code_from[i]] = code_to[i]

    for i in a:
        result += code[i]

    return result


phrase_original, phrase_coded, to_code, to_decode = (input() for _ in '1234')

print(code_decode(to_code, False, phrase_original, phrase_coded))
print(code_decode(to_decode, True, phrase_original, phrase_coded))
 