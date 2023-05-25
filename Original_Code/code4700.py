# put your python code here
def check_brackets(line):
    open_brackets = '({['
    close_brackets = ')}]'
    pairs = dict(zip(open_brackets, close_brackets))
    reverse_pairs = dict(zip(close_brackets, open_brackets))

    prefix, stack = '', []
    for c in line:
        if c in open_brackets:
            stack.append(pairs[c])
        elif stack:
            if c != stack[-1]:
                return 'IMPOSSIBLE'
            stack.pop()
        else:
            prefix = reverse_pairs[c] + prefix
    else:
        while stack:
            line = line + stack.pop()
        return prefix + line


print(check_brackets(input())) 