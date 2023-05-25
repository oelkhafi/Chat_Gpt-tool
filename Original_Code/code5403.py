#!/usr/bin/env python3
# coding=utf-8


import heapq
import collections


class PriorityQueue:
    def __init__(self, queue=[], compare=lambda x: x):
        self.compare = compare
        self.queue = [(self.compare(item), count, item) for count, item in enumerate(queue)]
        self.counter = len(self.queue)
        heapq.heapify(self.queue)

    def __len__(self):
        return len(self.queue)

    def push(self, item):
        heapq.heappush(self.queue, (self.compare(item), self.counter, item))
        self.counter += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


def build_tree(string):
    frequencies = collections.defaultdict(int)

    for ch in string:
        frequencies[ch] += 1

    pq = PriorityQueue((Leaf(ch, frequencies[ch]) for ch in frequencies), lambda x: x.get_frequency())

    while len(pq) > 1:
        first, second = pq.pop(), pq.pop()
        pq.push(Node(first, second))

    # return root of a Huffman binary tree
    return pq.pop()


class HuffmanEncoder:
    def __init__(self, string):
        self.root = build_tree(string)
        self.code = {}
        self.root.walk(self.code, """")

    def get_code(self):
        return self.code


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = left.freq + right.freq

    def get_frequency(self):
        return self.freq

    def walk(self, code, acc):
        self.left.walk(code, acc + ""0"")
        self.right.walk(code, acc + ""1"")


class Leaf:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def get_frequency(self):
        return self.freq

    def walk(self, code, acc):
        code[self.char] = acc or ""0""


def main():
    string = input()
    henc = HuffmanEncoder(string)
    code = henc.get_code()
    encoded_string = """".join(code[ch] for ch in string)

    print(len(code.items()), len(encoded_string))
    for ch in sorted(code):
        print(""{}: {}"".format(ch, code[ch]))

    print(encoded_string)


if __name__ == ""__main__"":
    main()
 