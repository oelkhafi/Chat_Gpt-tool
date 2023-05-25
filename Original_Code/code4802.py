import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def self_attention(features, proj_k, bias_k, proj_q, bias_q, proj_v, bias_v):
    """"""
    features - InLen x EmbSize - features of elements of input sequence
    proj_k - EmbSize x EmbSize - projection matrix to make keys from features
    bias_k - EmbSize - bias vector to make keys from features
    proj_q - EmbSize x EmbSize - projection matrix to make queries from features
    bias_q - EmbSize - bias vector to make queries from features
    proj_v - EmbSize x EmbSize - projection matrix to make values from features
    bias_v - EmbSize - bias vector to make values from features

    returns InLen x EmbSize
    """"""
    def softmax(x):
        return np.exp(x) / np.exp(x).sum(axis=1)[..., None]
    
    
    return softmax((features @ proj_q + bias_q) @ (features @ proj_k + bias_k).T) @ (features @ proj_v + bias_v)


features = read_array()
proj_k = read_array()
bias_k = read_array()
proj_q = read_array()
bias_q = read_array()
proj_v = read_array()
bias_v = read_array()

result = self_attention(features, proj_k, bias_k, proj_q, bias_q, proj_v, bias_v)

write_array(result) 