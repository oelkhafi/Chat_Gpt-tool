import sys

stack = [0]

for _ in range(int(sys.stdin.readline())):
	command = sys.stdin.readline().split()

	if command[0] == 'push':
		stack.append(max(stack[-1], int(command[1])))

	elif command[0] == 'pop':
		del stack[-1]

	else:
		print(stack[-1])











 