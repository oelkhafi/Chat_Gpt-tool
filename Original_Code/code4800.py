import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def softmax(x):
    """"""
    x - vector of n elements - input

    returns vector of n elements - softmax output
    """"""
    return np.exp(x) / np.exp(x).sum()


x = read_array()

result = softmax(x)

write_array(result)
 