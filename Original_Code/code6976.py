# put your python code here


n = int(input())
result = []
result.append(n)


def num_collatz(n):
    if n == 1:
        result.append(n)
        return
    if n%2 == 0:
        n = int(n/2)
        result.append(n)
        if n == 1:
            return
    if n%2 != 0:
        n = (n*3) + 1
        result.append(n)
    if n == 1:
        return
    num_collatz(n)


if n != 1:
    num_collatz(n)

for i in result:
    print(i, end=' ')






 