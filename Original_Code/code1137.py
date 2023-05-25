from functools import partial
from operator import __eq__

# you are only asked to implement functions myAll, myAny, elem
def booleanHelper(s, boolValue):
    ''' For a got sequence of boolean return if the sequence
        contains the specified value.
        s - iterable, sequence.
        boolValue - boolean, value to find.
    '''
    try:
        nextVal = next(s)
        return True if nextVal == boolValue else booleanHelper(s, boolValue)
    except:
        return False
    return False

def myAll(pred, s):
    return not booleanHelper(map(pred, s), False)

def myAny(pred, s):
    return booleanHelper(map(pred, s), True)


elem = lambda x: partial(myAny, partial(__eq__, x)) 