def convert(num, to_base=10, from_base=10):
    num = int(str(num), base=from_base)
    if to_base==10:
        return num
    else:
        alphabet = ""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ""
        answer = """"
        while num:
            rest = num%to_base
            answer+=alphabet[rest]
            num = num//to_base
        return answer[::-1]

def kaprekar10(n):
    N = n**2
    dev=10
    num = N
    ost = 0
    for i in range(1,len(str(N))):
        num = N // dev
        ost = N % dev
        if(ost > 0 and num+ost==n):return True
        dev *= 10
    return False

def kaprekar(num, base=10):
    if(base==10):return kaprekar10(int(num))
    if num in[1,'1']:return True
    N = convert(convert(num,10,base)**2,base,10) #Переводим из base в 10-ю, возводим в степень и возвращаем в base
    for i in range(1,len(N)):
        size = len(N) - i
        tmp=int(convert(N[:size],10,base)) + int(convert(N[size:],10,base))
        if(convert(str(tmp),base,10) in[num]): return True

    return False 