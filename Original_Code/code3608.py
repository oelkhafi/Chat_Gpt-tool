def convert_10(num, to_base=10, from_base=10): 
    # заводим список для замены больих остатков
    list_row = [ 0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L',
                'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

    num = int(num)
    s = ''   # строка в которую будем записывать результат
    if int(to_base)>=2 and int(to_base)<=36 :
        if type(num) == int:    # Проверяем тип числа
            num_a = num         # Заводим временную переменную, над которой будем производить действия в цикле  
            while num_a//to_base!=0:   # До тех пор пока целочисленное деление не равно нулю
                if num_a//to_base < to_base:   # Если целочисленное деление от степени(в которую приводим) меньше этой степени
                    if len(str(num_a%to_base))<2 and len(str(num_a//to_base))<2:  # Проверяем остаток на наличие, если остаток не 2-х значное число
                        s+=str(num_a % to_base)    # Добавляем в переменную s остаток т деление и целочисленное деление
                        s+=str(num_a // to_base)
                    else:
                        s+= str(list_row[num_a%to_base])   # Если если остаток 2-х значное число
                        if len(str(num_a // to_base))<2:
                            s+=str(num_a // to_base)            # Находим в списке соответствие числа и буквы
                        else:
                            s+=str(list_row[num_a // to_base])
                else:
                    if len(str(num_a%to_base))<2:
                        s+= str(num_a % to_base)       # Если целочисленное деление от степени(в которую приводим) больше этой степени
                    else:
                        s+= str(list_row[num_a%to_base])   # Если если остаток 2-х значное число
                num_a = num_a // to_base          # Записываем в переменную num_a остаток от деления
                
            return s[::-1]
    else:
        return ''
        
## Если число находится в десятичной системе счисления, то переводим её в заданную.
## Если число не в десятичной системе счисления, то переводим её в десятичную, а из десятичной в заданную
def convert(num, to_base=10, from_base=10):

    if from_base == 10:
        return convert_10(num, to_base, from_base)
    else:
        return convert_full(num, to_base, from_base)

        
def convert_full(num, to_base=10, from_base=10):
    list_row_1 = { 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,
                'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35 }
    N = []
    if int(to_base)>=2 and int(to_base)<=36 :
        L =  [ str(num)[i] for i in range(len(str(num))) ]
        for i in range(len(L)):
            try:
                if type(int(L[i])) == int:
                    N.append(int(L[i]))
            except:
                N.append(list_row_1[L[i]])
    
        A = sum([ int(N[i]*from_base**(len(N)-1-i)) for i in range(len(N)) ])

        return convert_10(A, to_base, from_base)
    else:
        return '' 