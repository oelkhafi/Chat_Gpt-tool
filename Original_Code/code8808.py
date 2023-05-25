# put your python code here
def check(_str):
    result = []
    opening = ""([{""
    closing = "")]}""
    numbers = []
    for i in range(len(_str)):
        if _str[i] not in opening and _str[i] not in closing:
            continue
        else:
            if _str[i] in opening:
                result.append(_str[i])
                numbers.append(i + 1)
            else:
                if len(result) == 0:
                    return i + 1
                top = result.pop()
                numbers.pop()
                if (top == ""("" and _str[i] != "")"") or \
                        (top == ""["" and _str[i] != ""]"") \
                        or (top == ""{"" and _str[i] != ""}""):
                    return i + 1

    if len(result) == 0:
        return ""Success""
    else:
        return numbers[-1]


print(check(input()))
 