import sys
import ast
import numpy as np
import scipy.sparse


def read_array():
    return ast.literal_eval(sys.stdin.readline())


def write_array(arr):
    print(repr(arr.tolist()))


def generate_coocurrence_matrix(texts, vocab_size):
    """"""
    texts - list of lists of ints - i-th sublist contains identifiers of tokens in i-th document
    vocab_size - int - size of vocabulary
    returns scipy.sparse.dok_matrix
    """"""
    return scipy.sparse.dok_matrix([[sum([i in s and j in s for s in texts if i != j])
                                     for i in range(vocab_size)] for j in range(vocab_size)])


text = read_array()
vocab_size = int(sys.stdin.readline().strip())

result = generate_coocurrence_matrix(text, vocab_size)

write_array(result.toarray())
 