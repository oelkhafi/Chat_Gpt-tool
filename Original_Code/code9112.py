import sys
import ast
import numpy as np
from numpy.linalg import norm

def parse_array(s):
    return np.array(ast.literal_eval(s))

def read_array():
    return parse_array(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def get_nearest(embeddings, query_word_id, get_n):
    """"""
    embeddings - VocabSize x EmbSize - word embeddings
    query_word_id - integer - id of query word to find most similar to
    get_n - integer - number of most similar words to retrieve

    returns list of `get_n` tuples (word_id, similarity) sorted by descending order of similarity value
    """"""
    dist = []
    q_emb = embeddings[query_word_id]
    for w_id, w_emb in enumerate(embeddings):
        dist.append((w_id, - norm(q_emb/norm(q_emb) - w_emb/norm(w_emb))))
    
    return sorted(dist, key=lambda x:x[1], reverse=True)[:min(get_n, len(embeddings))]


embeddings = read_array()
query_word_id = int(sys.stdin.readline().strip())
get_n = int(sys.stdin.readline().strip())

result = get_nearest(embeddings, query_word_id, get_n)

write_array(np.array(result)) 