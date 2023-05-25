import ast
import sys
import collections
import numpy as np


LayerInfo = collections.namedtuple('LayerInfo', ('kernel_size', 'dilation'))


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())


def calculate_receptive_field(layers):

    return calculate_receptive_field(layers[1:]) + layers[0][1] * (layers[0][0] - 1) if layers else 1


kernels = read_array()
dilations = read_array()

layers = [LayerInfo(k, d) for k, d in zip(kernels, dilations)]

result = calculate_receptive_field(layers)
print(result) 