#!/usr/bin/env python3

import re

exceptions = {}

except_stack = []

garbage = []


def add(arg):
    arg = re.findall(r'[\w]+', arg)
    exception = arg.pop(0)
    exceptions[exception] = {'parents': []}
    for el in arg:
        exceptions[exception]['parents'].append(el)


def get(exception):
    for parent in exceptions[exception]['parents']:
        if parent in except_stack and arg not in garbage:
            garbage.append(arg)
        else:
            get(parent)


for i in range(0, int(input())):
    add(input())


for i in range(0, int(input())):
    arg = input()
    except_stack.append(arg)
    get(arg)


for el in garbage:
    print(el)
 