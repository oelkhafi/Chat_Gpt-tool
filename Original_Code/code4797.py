import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))


def read_array():
    return parse_array(sys.stdin.readline())


def write_array(arr):
    print(repr(arr.tolist()))


def apply_convolution(data, kernel, bias):
    """"""
    data - InLen x InChannels
    kernel - OutChannels x InChannels x KernelSize
    bias - OutChannels

    returns OutLen x OutChannels
    """"""
    return np.array(
        [bias[oc] + np.array([sum(sum(data[pos+k, ic] * kernel[oc, ic, k]
        for ic in range(kernel.shape[1]))
        for k in range(kernel.shape[2]))
        for pos in range(data.shape[0] - kernel.shape[2] + 1)])
        for oc in range(kernel.shape[0])]).T


data = read_array()
kernel = read_array()
bias = read_array()

result = apply_convolution(data, kernel, bias)

write_array(result)
 