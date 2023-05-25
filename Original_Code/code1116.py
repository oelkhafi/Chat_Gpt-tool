def addCharToRes(res, c, count):
    if c:
        if count > 1:
            res.append(str(count))
        res.append(curChar)
            
            
s = input()
res = []
curChar = None
curCount = 0
for c in s:
    if curChar != c:
        addCharToRes(res, curChar, curCount)
        curCount = 1
        curChar = c
    else:
        curCount += 1

if curChar:
    addCharToRes(res, curChar, curCount)
    
print("""".join(res)) 