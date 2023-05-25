str = input()

pat = ('(', ')', '{', '}', '[', ']')
dic = {')': '(', '}': '{', ']': '['}
stack = []
result = 'Success'
for i, ch in enumerate(str):
    if ch not in pat:
        continue
    elif ch not in dic and i != len(str) - 1:
            stack += [[i, ch]]
    elif len(stack) != 0 and stack[-1][1] == dic[ch]:
        stack.pop()
    else:
        result = i + 1        
        break
    
if i == len(str) - 1 and len(stack) != 0 and result == 'Success':
    result = stack[-1][0] + 1
print(result)
 