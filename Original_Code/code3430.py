# put your python code here
str = input()
stack = []
count = []
for j, i in enumerate(str):
    if i == '(' or i == '[' or i =='{':
        stack.append(i)
        count.append(j)
    if i == ')' or i == ']' or i == '}':
        if stack:
            if i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[' or i == '}' and stack[-1] == '{':
                stack.pop()
                count.pop()
            else:
                print(j+1)
                quit()
        else:
            stack.append(i)
            count.append(j)
            break
if stack:
    print(count[-1] + 1)
else:
    print('Success') 