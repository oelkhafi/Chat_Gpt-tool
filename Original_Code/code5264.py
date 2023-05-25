n = int(input())
mas = []
arr = [] # 0 команда
arr.append([])# 0 команда
arr.append([])# 1 всего игр
arr.append([])# 2 побед
arr.append([])# 3 ничьих
arr.append([])# 4 поражений
arr.append([])# 5 всего очков
for i in range(0,n):
    b, index1 = False,0
    mas = []
    [mas.append(i.strip()) for i in input().strip().split("";"",3)]
    for index, item in enumerate(arr[0]):
        if item == mas[0]:#сущ ли эл в массиве
            index1 = index
            b = True
    if b == False:
        arr[0].append(mas[0])
        arr[1].append(1)
        if mas[1]>mas[3]:
            arr[2].append(1)
            arr[5].append(3)
            arr[3].append(0)
            arr[4].append(0)
        elif mas[1]==mas[3]:
            arr[3].append(1)
            arr[5].append(1)
            arr[2].append(0)
            arr[4].append(0)
        else:
            arr[4].append(1)
            arr[5].append(0)
            arr[3].append(0)
            arr[2].append(0)
    else:
        arr[1][index1]+=1#всего игр
        if mas[1]>mas[3]:
            arr[2][index1]+=1
            arr[5][index1]+=3
            arr[3][index1]+=0
            arr[4][index1]+=0
        elif mas[1]==mas[3]:
            arr[3][index1]+=1
            arr[5][index1]+=1
            arr[2][index1]+=0
            arr[4][index1]+=0
        else:
            arr[4][index1]+=1
            arr[5][index1]+=0
            arr[3][index1]+=0
            arr[2][index1]+=0
        #вторая команда
    b = False
    for index, item in enumerate(arr[0]):
        if item == mas[2]:#сущ ли эл в массиве
            index1 = index
            b = True
    if b == False:
        arr[0].append(mas[2])
        arr[1].append(1)
        if mas[3]>mas[1]:
            arr[2].append(1)
            arr[5].append(3)
            arr[3].append(0)
            arr[4].append(0)
        elif mas[3]==mas[1]:
            arr[3].append(1)
            arr[5].append(1)
            arr[2].append(0)
            arr[4].append(0)
        else:
            arr[4].append(1)
            arr[5].append(0)
            arr[3].append(0)
            arr[2].append(0)
    else:
        arr[1][index1]+=1#всего игр
        if mas[3]>mas[1]:
            arr[2][index1]+=1
            arr[5][index1]+=3
            arr[3][index1]+=0
            arr[4][index1]+=0
        elif mas[1]==mas[3]:
            arr[3][index1]+=1
            arr[5][index1]+=1
            arr[2][index1]+=0
            arr[4][index1]+=0
        else:
            arr[4][index1]+=1
            arr[5][index1]+=0
            arr[3][index1]+=0
            arr[2][index1]+=0
for i in range(0,len(arr[0])):
    print(str(arr[0][i])+"":""+str(arr[1][i]),str(arr[2][i]),str(arr[3][i]),str(arr[4][i]),str(arr[5][i])) 