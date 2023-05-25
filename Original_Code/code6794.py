#!/usr/bin/env python3

key = {}

def encode(string):
    r = ''
    for i in string:
        r += key[i]
    return r

def decode(string):
    r = ''
    deKey = {v : k for k, v in key.items()}
    for i in string:
        r += deKey[i]
    return r

stringOr, stringK = input(), input()

for i in range(len(stringOr)):
    key[stringOr[i]]=stringK[i]

print(encode(input()))
print(decode(input()))
 