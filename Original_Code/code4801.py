import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def dsoftmax_dx(x):
    """"""
    x - vector of n elements - input

    returns matrix n x n
    """"""
    sm = np.exp(x) / np.exp(x).sum()
    result = np.zeros((x.size, x.size))
    for i in range(x.size):
        for j in range(x.size):
            if i == j:
                result[i, j] = sm[i] * (1 - sm[i])
            else:
                result[i, j] = - sm[i] * sm[j]
    return result


x = read_array()

result = dsoftmax_dx(x)

write_array(result)
 