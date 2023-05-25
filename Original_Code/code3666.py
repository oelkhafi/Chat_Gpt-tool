buffer = []
log = []

def clearBuffer(arrival, buffer):
    temp = []
    for i in range(len(buffer)):
        if buffer[i][1] > arrival:
            temp.append(buffer[i])
    return temp

size, n = map(int, input().split())

for i in range(n):
    #if i > 0: print(buffer)
    arrival, duration = map(int, input().split())

    #Удаляем все обработанные пакеты, если такие есть
    if len(buffer) > 0:
        if buffer[0][1] <= arrival:
            buffer = clearBuffer(arrival, buffer)

    #если буфер заполнен
    if len(buffer) == size:
        log.append(-1)

    if len(buffer) == 0:
        buffer.append([arrival, arrival + duration])
        log.append(arrival)
    elif len(buffer) < size:
        if buffer[-1][1] > arrival:
            arrival_new = buffer[-1][1]
        else:
            arrival_new = arrival
        buffer.append([arrival_new, arrival_new + duration])
        log.append(arrival_new)

for l in log:
    print(l)


 