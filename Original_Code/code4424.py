a, b, c, d = (int(input()) for _ in range(4))
spr = '\t'

for x in range (c, d+1):  # слева на право
    print(spr + str(x), end='')
print(end='\n')

for y in range (a, b+1):  # сверху вниз
    print(str(y) + spr, end='')
    for j in range (c, d+1):
        print(str(y * j), end=spr)  # заполняем таблицу
    print(end='\n')



# a, b = от и до вертикаль
# с, d = от и до горизонт




# for i in range(a-1, b):
#     i += 1
#     print(i)
#
# for x in range(c-1, d):
#     x += 1
#     print(x, end='\t') 