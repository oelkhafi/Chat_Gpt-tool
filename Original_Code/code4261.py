# put your python code here
def hash(s):
    sum = 0
    for i in range(len(s)):
        sum = (sum + (ord(s[i]) * xh[i]) % p) % p
    return sum

pattern = input()
text =  input()
x = 23
p = 1000000007
xh = [1]
for i in range(1,len(pattern)):
    xh.append(xh[i-1]*x % p)
patternh = hash(pattern)
curh = hash(text[len(text)-len(pattern):])
res = []
for i in range(len(text)-len(pattern),-1,-1):
    if curh == patternh and pattern == text[i:i+len(pattern)]:
        res.append(i)
    if i>0:
        curh = (curh - ord(text[i+len(pattern)-1])*xh[len(pattern)-1]) % p
        curh = (curh + p) % p
        curh = (curh * x) % p
        curh = (curh + ord(text[i-1])) % p
print(*res[::-1]) 




 