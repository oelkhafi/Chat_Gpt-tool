import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def generate_w2v_sgns_samples(text, window_size, vocab_size, ns_rate):

    result = []
    pad = window_size // 2

    for w_idx, word in enumerate(text):
        for c_idx in range(w_idx-pad, w_idx+pad+1):
            if 0 <= c_idx < len(text) and c_idx != w_idx:
                result.append([word, text[c_idx], 1])
                for _ in range(ns_rate):
                    result.append([word, np.random.randint(vocab_size), 0])

    return result


text = read_array()
window_size = int(sys.stdin.readline().strip())
vocab_size = int(sys.stdin.readline().strip())
ns_rate = int(sys.stdin.readline().strip())

result = generate_w2v_sgns_samples(text, window_size, vocab_size, ns_rate)

write_array(np.array(result)) 