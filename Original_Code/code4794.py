import sys
import ast
import numpy as np


def parse_array(s):
    return np.array(ast.literal_eval(s))


def read_array():
    return parse_array(sys.stdin.readline())


def write_array(arr):
    print(repr(arr.tolist()))


def update_ft_weights(center_embeddings, context_embeddings,
                      center_subwords, context_word,
                      label, learning_rate):
    """"""
    center_embeddings - VocabSize x EmbSize
    context_embeddings - VocabSize x EmbSize
    center_subwords - list of ints - list of identifiers of n-grams contained in center word
    context_word - int - identifier of context word
    label - 1 if context_word is real, 0 if it is negative
    learning_rate - float > 0 - size of gradient step
    """"""
    def delta(a, b):
        return (pow(1 + np.exp(-(a * b).sum()), -1) - label) * b * learning_rate

    center_delta = delta(
        center_embeddings[center_subwords].mean(axis=0),
        context_embeddings[context_word]
        )
    context_delta = delta(
        context_embeddings[context_word],
        center_embeddings[center_subwords].mean(axis=0)
        )

    center_embeddings[center_subwords] -= center_delta / len(center_subwords)
    context_embeddings[context_word] -= context_delta


center_embeddings = read_array()
context_embeddings = read_array()
center_subwords = read_array()
context_word = int(sys.stdin.readline().strip())
label = int(sys.stdin.readline().strip())
learning_rate = float(sys.stdin.readline().strip())

update_ft_weights(center_embeddings, context_embeddings,
                  center_subwords, context_word, label, learning_rate)

write_array(center_embeddings)
write_array(context_embeddings)
 