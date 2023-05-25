#import logging.config
from collections import deque

OPEN_BRACKETS = {'(': 0, '{': 1, '[': 2}
CLOSE_BRACKETS = {')': 0, '}': 1, ']': 2}

#logging.config.fileConfig(abs_path('logging.cfg'))
#logger = logging.getLogger('first_week')


def brackets_checker(line):
    stack = deque()
    for i, bracket in enumerate(line, 1):
        # logger.debug('Current bracket: {}'.format(bracket))
        if bracket in OPEN_BRACKETS:
            # Put open brackets in stack
            stack.append((i, bracket))
            # logger.debug('Current stack: {}'.format(stack))
        elif bracket in CLOSE_BRACKETS:
            # On close bracket encounter
            # If stack is empty close bracket is invalid
            if not len(stack):
                return i
            # Else pop last bracket
            popped_i, popped_bracket = stack.pop()
            # logger.debug('Popped bracket: {}'.format(popped_bracket))
            # Compare brackets
            # If they are not equal, return real position of current bracket
            # logger.debug('Current stack: {}'.format(stack))
            if CLOSE_BRACKETS[bracket] != OPEN_BRACKETS[popped_bracket]:
                return i
    if len(stack):
        # If there are some brackets left, return real position of the leftmost not closed bracket
        return stack.popleft()[0]
    else:
        return 'Success'


if __name__ == '__main__':

    line = input()
    res = brackets_checker(line)
    print(res)
 