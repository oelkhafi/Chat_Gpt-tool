script = {}

s = '''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000'''

#создаем словарь с таблицей значений
for line in s[1:].splitlines():
    key, value = line.split(' = ')
    script[key] = int(value)

s = input()
dec = [script[i] for i in s]

res, tmp = 0, 0
for i in range(len(s) - 1):
    if dec[i] // dec[i + 1] < 10:
        if dec[i] < dec[i + 1]:
            tmp = dec[i + 1] - dec[i] if not tmp else dec[i + 1] - tmp
        else:
            tmp += dec[i + 1] + dec[i] if not tmp else dec[i + 1]
    else:
        res += dec[i] if not tmp or not i else tmp
        tmp = 0 if len(s) - 1 - i > 1 else dec[i + 1]
print(dec[0] if len(s) == 1 else res + tmp)
 