number = int(input())
dictionary = []
english = {}
spanish = {}
for counter in range(number):
    dictionary.append([x for x in input().split(' - ')])
    english[dictionary[-1][0]] = dictionary[-1][1].split(', ')
for counter in english.keys():
    for counter2 in english[counter]:
        if counter2 not in spanish.keys():
            spanish[counter2] = [counter]
        else:
            spanish[counter2].append(counter)
print(len(spanish))
for counter in sorted(spanish.keys()):
    spanish[counter].sort()
    print(counter + ' -', end = ' ')
    for counter2 in range(len(spanish[counter])):
        if len(spanish[counter]) == 1:
            print(spanish[counter][counter2], end = '')
        elif counter2 == len(spanish[counter]) - 1:
            print(spanish[counter][counter2], end = '')
        else:
            print(spanish[counter][counter2] + ',', end = ' ')
    print()
 