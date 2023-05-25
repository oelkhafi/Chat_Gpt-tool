def makekey (a, b):
    r = [-1 for i in range(256)]
    for i in range (len (a)):
        r [ord (a [i])] = ord (b [i])
    return r
def replace (k, s):
    r = ''
    for i in range (len (s)):
        p = ord (s [i])
        if k [p] >= 0:
            r += chr (k [p])
        else:
            r += s [i]
    return r
x = input()
y = input()
print (replace (makekey (x, y), input()))
print (replace (makekey (y, x), input()))




 