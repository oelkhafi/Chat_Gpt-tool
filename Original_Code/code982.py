def main():
    impossible = """"
    seq = input()
    d = dict(zip( ['{', '(', '[', '}', ')', ']'], ['}', ')', ']', '{', '(', '['] ))
    opens = '{(['
    closes = '})]'
    stack = []
    for bracket in seq:
        if stack and (stack[-1] in opens) and (bracket in closes):
            if d[stack[-1]] == bracket: stack.pop()
            else:
                impossible = 'IMPOSSIBLE'
                break
        else: stack.append(bracket)
    ladd = radd = """"
    for bracket in stack:
        if bracket in opens: break
        else: ladd = d[bracket] + ladd
    for bracket in stack[::-1]:
        if bracket in closes: break
        else: radd += d[bracket]
    print(ladd+seq+radd if not impossible else impossible)

if __name__ == ""__main__"": main()  