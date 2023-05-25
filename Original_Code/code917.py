smallletter = 'abcdefghijklmnopqrstuvwxyz'
s = set()
ss = set()
n = int(input())
for _ in range(n):
    inp = input() 
    s|={inp}
    ss|={inp.lower()}
err = 0
try:
    inp = input().split()
except EOFError as e:
    inp = ''
for w in inp:
    if w not in s:
        if w.lower() in ss:
            err += 1
        else:
            ems = 0
            for ltr in w:
                if ltr not in smallletter:
                    ems += 1
                    if ems > 1:
                        break
            if ems != 1:
                err += 1        
print(err)  