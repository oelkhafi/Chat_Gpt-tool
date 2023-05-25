def math_interpreter(expression):
    commands = ['plus', 'minus', 'multiply', 'divide']
    first, command, second = expression.split()
    first, second = int(first), int(second)
    if command not in commands:
        return f'Unknow command: ""{command}"".'
    if command == 'plus':
        result = first + second
    elif command == 'minus':
        result = first - second
    elif command == 'multiply':
        result = first * second
    elif second == 0:
        return f'Error: ""Zero divide""'
    else:
        result = first // second
    return result


if __name__ == '__main__':
    print(math_interpreter(input())) 