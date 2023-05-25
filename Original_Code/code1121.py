def checkBrackets(s):
    ''' str => int
        Return None - if any close bracket has proper open bracket
        and any open bracket has proper close bracket.
        Return position of bracket without it's pair.
    '''
    # get character of open bracket
    # by the char of close bracket
    openBrackets =  ""{[(""
    closeToOpenBrackets = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<' }
    # stack to store previous not closed brackets
    stack = []
    # stack to store indices respect to characters in stack.
    # It needs to detect error position in the string s.
    stackIdx = []
    slen = len(s)
    for idx in range(0, slen):
        c = s[idx]
        if c in openBrackets:
            stack.append(c)
            stackIdx.append(idx)
        elif c in closeToOpenBrackets:
            # c is the close bracket.
            # last bracket in the stack
            # must be proper open bracket
            if len(stack) == 0:
                return idx+1
            mybeOpenBracket = stack.pop()
            openBracketMatch = closeToOpenBrackets[c]
            if mybeOpenBracket != openBracketMatch:
                return idx+1
            stackIdx.pop()
        #else we pass any other character
    if len(stackIdx) > 0:
        return stackIdx[-1]+1
    return None


def testBrackets(s):
    errPosition = checkBrackets(s)
    if errPosition:
        return errPosition
    else:
        return ""Success""


s = input()
print(testBrackets(s)) 