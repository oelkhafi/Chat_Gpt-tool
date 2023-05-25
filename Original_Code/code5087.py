#!/usr/bin/python3
import bisect


class PriorityQueue():

    def __init__(self):
        self.__queue = []

    def add(self, num):
        bisect.insort(self.__queue, num)

    def get(self):
        print(self.__queue.pop())

if __name__ == '__main__':
    queue = PriorityQueue()
    for i in range(int(input())):
        operation = input()
        if operation == ""ExtractMax"":
            queue.get()
        else:
            queue.add(int(operation.split()[-1]))
 