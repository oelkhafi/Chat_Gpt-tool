from collections import Counter
s = input()
c = Counter(s)
k = len(c)
if k<3:
    print(k,len(s))
    for i,ch in enumerate(c):
        print('{}: {}'.format(ch,i))
        s = s.replace(ch,str(i))
else:
    h,code = list(c.items()),{}
    for i in range(k-1):
        m1 = min(h,key = lambda x: x[1])
        h.remove(m1)
        m2 = min(h,key = lambda x: x[1])
        h.remove(m2)
        h.append((m1[0]+m2[0],m1[1]+m2[1]))
        for l1 in m1[0]:
            if l1 in code.keys():
                code[l1] += '0'
            else:
                code[l1] = '0'
        for l2 in m2[0]:       
            if l2 in code.keys():
                code[l2] += '1'
            else:
                code[l2] = '1'
    for ch in code:
        s = s.replace(ch,code[ch][::-1])
    print(k,len(s))
    for ch in code:
        print('{}: {}'.format(ch,code[ch][::-1]))
print(s) 