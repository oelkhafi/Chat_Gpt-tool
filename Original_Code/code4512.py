number = int(input())
matrix = []
teams = {}
for counter in range(number):
    string = [x for x in input().split(';', maxsplit = 4)]
    for counter in string[::2]:
        if counter not in teams.keys():
            teams[counter] = [0, 0, 0, 0, 0]
    if int(string[1]) > int(string[3]):
        teams[string[0]][0] += 1
        teams[string[0]][1] += 1
        teams[string[0]][4] += 3
        teams[string[2]][0] += 1
        teams[string[2]][3] += 1
    elif int(string[1]) == int(string[3]):
        teams[string[0]][0] += 1
        teams[string[0]][2] += 1
        teams[string[0]][4] += 1
        teams[string[2]][0] += 1
        teams[string[2]][2] += 1
        teams[string[2]][4] += 1
    elif int(string[1]) < int(string[3]):
        teams[string[0]][0] += 1
        teams[string[0]][3] += 1
        teams[string[2]][0] += 1
        teams[string[2]][1] += 1
        teams[string[2]][4] += 3
matrix = teams.keys()
for counter in matrix:
    print(counter + ':', end = '')
    for counter2 in teams[counter]:
        print(counter2, end = ' ')
    print()
 