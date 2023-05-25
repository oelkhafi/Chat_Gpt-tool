# put your python code here
def decode(s, dic):
    n = ''
    for i in s:
        n += i
        if n not in dic.keys():
            pass
        else:
            print(dic[n], end='')
            n = ''


k, l = input().split()
d = {}
for i in range(int(k)):
    k, v = input().split(': ')
    d[v] = k
s = input()
decode(s, d)



 