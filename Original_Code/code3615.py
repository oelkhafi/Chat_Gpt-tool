n = int(input())
dict = {}
for i in range(n):
    k = input().split()
    # Проверка что класс не наследуется сам от себя
    if len(k)>2 and k[0] == k[2]:        
        dict[k[0]] = {}
    # Проверяется, что класс ни от чего не наследуется
    elif len(k) == 1:
        dict[k[0]] = {}
    # Проверяется ,что класс е в словаре
    elif k[0] not in dict:
        dict[k[0]] = set(k[2:]) 
    elif k[0] in dict:
        dict[k[0]].update(k[2:])    
        
m = int(input())

class Catapult(Exception):
    pass

def funс_recursion(first, lst, k, dict):
    if k in lst:
         lst.append(k)
         return k
    elif k not in lst: 
        if len(lst) == 0:
            pass
        else:
            for i in dict[k]:
                if funс_recursion(first, lst, i, dict) in lst:
                    lst.append(k)
                    return first
        

lst = []
for i in range(m):
    k = input()
    first = k
    if funс_recursion(first, lst, k, dict) is not None or funс_recursion(first, lst, k, dict) in lst:
        print(funс_recursion(first, lst, k, dict))
    if k not in lst:
        lst.append(k) 