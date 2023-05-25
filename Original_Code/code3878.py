def num(string):
    try:
        return int(string)
    except ValueError:
        return float(string)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div_norm(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Division by 0!'


def div_int(x, y):
    try:
        return x // y
    except ZeroDivisionError:
        return 'Division by 0!'


def mult(x, y):
    return x * y


def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return 'Division by 0!'


def _pow(x, y):
    return x ** y


OPERATIONS = {
    '+': add,
    '-': sub,
    '/': div_norm,
    '*': mult,
    'mod': mod,
    'div': div_int,
    'pow': _pow
}

a = num(input())
b = num(input())
operation = input()
print(OPERATIONS[operation](a, b))
 