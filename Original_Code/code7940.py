def readDictEntry():
    text = input().strip()
    temp = text.split(' - ')
    temp[1] = temp[1].split(', ')
    return temp
    
def digList(lst):
    temp = []
    for item in lst:
        if type(item) is list:
            temp.append(digList(item))
        else:
            temp.append(item)
    return set(temp)
    
n = int(input())
row = []
latin = []
latinDict = {}
engDict = {}
for i in range(n):    
    row = readDictEntry()
    latinDict[row[0]] = row[1]
    latin.extend(row[1])
    del row
latin = sorted(set(latin))
for k, v in latinDict.items():
    if type(v) is list:
        items = digList(v)
        for item in items:
            engDict[item] = engDict.get(item, [])
            engDict[item].append(k)
    else:
        engDict[v] = engDict.get(v, [])
        engDict[v].append(k)
print(len(latin))
for voc in latin:
    print(voc + "" - "" + ', '.join(val for val in sorted(engDict[voc]))) 