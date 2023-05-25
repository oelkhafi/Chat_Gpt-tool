import sys, random

def H(s,p):
    a = ord(s[0]) % 1000000007
    x = 1
    for i in range(1, len(s)):
        x = x * p % 1000000007
        a += ord(s[i]) * x % 1000000007
    return a % 1000000007

pattern = sys.stdin.readline().strip()
text = sys.stdin.readline().strip()


def rabinKarp (text, pattern):
    answer = []
    n = len(text)
    p = len(pattern)

    x = random.randint(1,p)

    hashText = H(text[n-p:n],x)
    hashPattern = H(pattern,x)
    xp = pow(x,p-1, 1000000007)

    for i in range(n-p-1,-1,-1):
        if hashText == hashPattern:
            answer.append(i+1)
        hashText = (hashText * (x % 1000000007) - (ord(text[i + p]) % 1000000007) * xp * (x % 1000000007) + ord(text[i]) % 1000000007) % 1000000007

    if hashText == hashPattern:
        answer.append(0)
    return answer

answer = rabinKarp(text,pattern)
a = []
for i in range(len(answer)-1,-1,-1):
    a.append(answer[i])

print(*a) 