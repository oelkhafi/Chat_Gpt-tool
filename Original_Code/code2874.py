def check_date(d):
    d = d.split('.')
    a = int(d[2]) % 4 == 0 and int(d[2]) % 100 != 0 or int(d[2]) % 400 == 0
    if int(d[1]) <= 12:
        if (d[1]in ['01','03','05','07','08','10','12'] and int(d[0]) <= 31) or(d[1]in ['04','06','09','11']
        and int(d[0]) <= 30):
            return ""Корректная""
    if a and int(d[0]) <= 29 and d[1] == '02':
        return ""Корректная""
    if a == False and int(d[0]) <= 28 and d[1] == '02':
        return ""Корректная""
    return ""Некорректная""
i = 0
while True:
    s = input()
    if s == '.':
        break
    s1 = check_date(s)
    if s1 == ""Корректная"":
        i += 1
    print(s1)
print(i) 