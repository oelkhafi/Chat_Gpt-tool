a = input()

dic1 = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
dic2 = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
b, i = 0, 0

while i <= len(a)-1:

    if i <= len(a)-2:
        d = a[i] + a[i+1]
         
    if (i <= len(a)-2) and(d in dic2):
        b = (dic2.get(d))+b
        i += 2
    elif (a[i] in dic1):
        b = dic1.get(a[i])+ b
        i += 1
print(b)
    
    
 