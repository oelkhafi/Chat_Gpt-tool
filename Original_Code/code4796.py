import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def update_glove_weights(x, w, d, alpha, max_x, learning_rate):
    """"""
    x - square integer matrix VocabSize x VocabSize - coocurrence matrix
    w - VocabSize x EmbSize - first word vectors
    d - VocabSize x EmbSize - second word vectors
    alpha - float - power in weight smoothing function f
    max_x - int - maximum coocurrence count in weight smoothing function f
    learning_rate - positive float - size of gradient step
    """"""
    def f(z):
        if z <= max_x:
            return pow(z / max_x, alpha)
        else:
            return 1.0
    
    F = np.apply_along_axis(f, 2, x[..., np.newaxis]).reshape(x.shape)
    Y = np.log(x + 1)

    dw = 2 * F * (w @ d.T - Y) @ d * learning_rate
    dd = (2 * F * (w @ d.T - Y)).T @ w * learning_rate

    w -= dw
    d -= dd


x = read_array()
w = read_array()
d = read_array()
alpha = float(sys.stdin.readline().strip())
max_x = int(sys.stdin.readline().strip())
learning_rate = float(sys.stdin.readline().strip())

update_glove_weights(x, w, d, alpha, max_x, learning_rate)

write_array(w)
write_array(d)
 