import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))


def read_array():
    return parse_array(sys.stdin.readline())


def write_array(arr):
    print(repr(arr.tolist()))


def update_w2v_weights(center_embeddings, context_embeddings,
                       center_word, context_word,
                       label, learning_rate):
    """"""
    center_embeddings - VocabSize x EmbSize
    context_embeddings - VocabSize x EmbSize
    center_word - int - identifier of center word
    context_word - int - identifier of context word
    label - 1 if context_word is real, 0 if it is negative
    learning_rate - float > 0 - size of gradient step
    """"""
    def delta(a, b):
        return (pow(1 + np.exp(-(a * b).sum()), -1) - label) * b * learning_rate

    center_delta = delta(center_embeddings[center_word], context_embeddings[context_word])
    context_delta = delta(context_embeddings[context_word], center_embeddings[center_word])

    center_embeddings[center_word] -= center_delta
    context_embeddings[context_word] -= context_delta


center_embeddings = read_array()
context_embeddings = read_array()
center_word = int(sys.stdin.readline().strip())
context_word = int(sys.stdin.readline().strip())
label = int(sys.stdin.readline().strip())
learning_rate = float(sys.stdin.readline().strip())

update_w2v_weights(center_embeddings, context_embeddings,
                   center_word, context_word, label, learning_rate)

write_array(center_embeddings)
write_array(context_embeddings)
 