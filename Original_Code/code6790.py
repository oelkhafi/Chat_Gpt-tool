#!/usr/bin/env python3
import re

classes = {}


def add(cl, parent=None, *args):
    classes[cl] = {'parent': [parent, ]}
    for el in args:
        classes[cl]['parent'].append(el)


def get(cl1, cl2):
    global reply
    if cl2 in classes:
        if cl1 == cl2:
            reply = ""Yes""
        for parent in classes[cl2]['parent']:
            if parent == cl1:
                reply = ""Yes""
                break
            else:
                if parent is not None:
                    get(cl1, parent)


for i in range(int(input())):
    args = input()
    args = re.split(r'\s:\s|\s', args)
    add(*args)

for i in range(int(input())):
    args = input().split()
    reply = ""No""
    get(*args)
    print(reply)
 