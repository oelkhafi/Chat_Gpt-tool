# put your python code here
n = int(input())
list = [[i for i in input().split(';')] for j in range(n)]
dict = {}
for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] not in dict and list[i][j].isdigit() == False:
            dict[list[i][j]] = [1, 0, 0, 0, 0]
            if int(list[i][j+1]) > int(list[i][j-1]):
                dict[list[i][j]][1] += 1
                dict[list[i][j]][4] += 3
            elif int(list[i][j+1]) == int(list[i][j-1]):
                dict[list[i][j]][2] += 1
                dict[list[i][j]][4] += 1
            else:
                dict[list[i][j]][3] += 1
        elif list[i][j] in dict and list[i][j].isdigit() == False:
            dict[list[i][j]][0] += 1
            if int(list[i][j+1]) > int(list[i][j-1]):
                dict[list[i][j]][1] += 1
                dict[list[i][j]][4] += 3
            elif int(list[i][j+1]) == int(list[i][j-1]):
                dict[list[i][j]][2] += 1
                dict[list[i][j]][4] += 1
            else:
                dict[list[i][j]][3] += 1
for k, v in dict.items():
    print(k+':', *v)



 