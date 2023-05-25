import numpy as np

def dynamic(item_count, capacity, items, debug=False):
    # dynamic algorithm
    d = np.zeros((capacity+1, item_count), dtype=int)
    value = 0
    weightLeft = capacity

    # установим для первого предмета ценность начиная
    # с емкосит способной его вместить
    d[items[0, 2]:, 0] = items[0, 1]
    
    for idx in range(1, item_count):
        prevIdx = idx - 1
        vi, wi = items[idx, 1:]
        # Все что меньше емкости текущего предмета
        # заполняем емкостями из предыдущей колонки.
        d[:wi-1, idx] = d[:wi-1, prevIdx]
        
        for curCap in range(wi, capacity+1):
            #Значение слева: если текущий предмет не используем.
            leftValue = d[curCap, prevIdx]
            #Значение по диагонали: если используем тек. предмет.
            diagValue = d[curCap - wi, prevIdx] + vi
            d[curCap, idx] = max(leftValue, diagValue)
            
    # Проходим обратно и собираем решение
    value = d[-1, -1]
    taken = np.full((item_count), ""0"", dtype=str)
    curCap = capacity
    idx = item_count-1
    while curCap > 0 and idx > 0:
        if d[curCap, idx] != d[curCap, idx-1]:
            #Текущий предмет был взят.
            taken[idx] = '1'
            curCap -= items[idx, 2]
        idx -= 1
        
    if curCap > 0 and d[curCap, 0]:
        taken[0] = '1'
    
    # prepare the solution in the specified output format
    outs = ' '.join(taken.flatten())
    if debug:
        allWeight = sum(map(lambda it: it[2], (filter(lambda it: taken[it[0]] == '1', items))))
        return ""{} 1\n{}"".format(value, outs), allWeight, taken, items, d
    return value, outs

def getItems(input_data, item_count):
    ''' items is [[idx, value, weight]] '''
    items = np.fromstring(input_data, dtype=int, sep=' ')
    i2 = items.copy()
    items = items.reshape((item_count,1))
    i3 = np.insert(items, 0, i2, axis=1)
    items = np.insert(i3, 0, range(0, item_count), axis=1)
    return items

getIntLine = lambda: map(int, input().split())

w,n = getIntLine()
items = getItems(input(), n)
value, outs = dynamic(n, w, items)

print(value)
 