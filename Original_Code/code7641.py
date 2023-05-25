d=""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ""

def a_to_dec(n, sys):
    k = 0
    for i in range(len(n)):
        k += d.find(n[len(n)-i-1])*sys**i
    return k

def dec_to_a(n, sys):
    a = int(n)
    s = ''
    while a // sys > 0:
        s = d[a % sys] + s
        a //= sys
    if a:
        s = d[a] + s
    return s

def convert(num, to_base=10, from_base=10): 
    if to_base == 10 and from_base == 10:
        return num
    elif to_base == 10:
        return str(a_to_dec(num, from_base))
    elif from_base == 10:
        return dec_to_a(num, to_base)
    else:
        return dec_to_a(str(a_to_dec(num, from_base)), to_base)
 