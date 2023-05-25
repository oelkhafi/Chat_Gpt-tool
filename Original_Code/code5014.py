n = int(input())
max_1 = 0
max_2 = 0
sa = 0
cnt = 0
while n:
    if n % 5 == 0:
        if n > max_1:
            max_1, max_2 = n, max_1
        elif n > max_2:
            max_2 = n
    if n % 3 == 0 or n % 10 == 9:
        cnt += 1
        sa += n
    n = int(input())
rez = 0
if cnt:
    rez = sa / cnt
print(max_2 if max_2 else ""NO"")
print(rez if rez else ""NO"")
     