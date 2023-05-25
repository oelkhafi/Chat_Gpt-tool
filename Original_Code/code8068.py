s=input()
types=['int', 'str', 'list']
if s in types:
    if s==types[0]:
        a,b = (int(input()) for i in range(2))
        if a or b: 
            print(a+b)
        else: 
            print(""Empty Ints"")
    if s==types[1]:
        a=input()
        if a: 
            print(a)
        else: 
            print('Empty String')
    if s==types[2]:
        a=input().split()
        if a: 
            print(a[-1])
        else: 
            print('Empty List')
else:
    print('Unknown type')




 