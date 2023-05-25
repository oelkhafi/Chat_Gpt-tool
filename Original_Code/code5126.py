import sys

buffer, free_time = [], 0
size, count = map(int, sys.stdin.readline().split())
for i in range(count):
    arrival, duration = map(int, sys.stdin.readline().split())
    while buffer and arrival >= buffer[0]:
        free_time = buffer[0]
        del buffer[0]
    if len(buffer) < size:
        time_exit = max(arrival, buffer and buffer[-1] or free_time)
        buffer.append(time_exit + duration)
        print(time_exit)
    else:
        print('-1')





 