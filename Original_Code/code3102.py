def foo(tmp2):
    last = buf[len(buf)-1][0]
    if tmp2 == ')' and last == '(':
        return True
    elif tmp2 == ']' and last == '[':
        return True
    elif tmp2 == '}' and last == '{':
        return True
    else:
        return False

buf = []
err = 0

s = input()
for i in range(len(s)):
    if s[i] in ')]}' and len(buf)==0:
        err = i+1
        break
    if s[i] in ')]}' and len(buf)>0:
        if foo(s[i]):
            buf.pop()
        else:
            err = i+1
            break
    if s[i] in '([{':
        buf.append([s[i], i+1])
if err == 0:
    if len(buf) == 0:
        print('Success')
    else:
        print(buf[len(buf)-1][1])
else:
    print(err)
     