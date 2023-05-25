# put your python code here
from collections import defaultdict

def hash(s):
    sum = 0
    for i in range(len(s)):
        sum = (sum + (ord(s[i]) * xh[i]) % p) % p
    return sum % m

m = int(input())
n = int(input())
d = defaultdict(list)
x = 263
p = 1000000007
xh = [1]
for i in range(1,16):
    xh.append(xh[i-1]*x % p)
for i in range(n):
    words = input().split()    
    if  words[0]=='check':  print(*d[int(words[1])])
    else:
        h = hash(words[1])
        if words[0]=='add' and words[1] not in d[h]: 
            d[h].insert(0,words[1])
        elif words[0]=='find': 
            print('yes' if words[1] in d[h] else 'no')
        elif  words[0]=='del' and words[1] in d[h]:
                d[h].remove(words[1])



 