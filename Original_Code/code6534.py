import sys

next(sys.stdin)
nums = [int(num) for num in next(sys.stdin).strip().split()]

res_dict, res = dict(), 0
#реализация через словарь res_dict, 
#key - последний элемент подпоследовательности, value - длина подпоследовательности
#res - инвариант: ""в каждый момент времени показывает длину наибольшей подпоследовательности""
#res - это просто максимум, который нужно вывести в конце
for i,num in enumerate(nums):   #однопроходный алгоритм
    sub_seq = 0                 #subsequence подпоследовательность
    for key,value in res_dict.items():
        if num % key == 0 and value > sub_seq:
            sub_seq = value    
    res_dict[num] = sub_seq + 1

    if sub_seq +1 > res:        #подсчет максимума за один проход
        res = sub_seq +1
    
print(res)
 