klu, klu1={}, {}
n=0
s, s1 = [], []
a=input()
a1=input()
a2=input()
a3=input()
for i in a: # пtреводим в словарь для шифрования
    klu[i]=a1[n]
    n+=1
n=0
for i in a2: # шифруем все
    s.append(klu[i])
for i in a1: # переводим зашифрованный в словарь
    klu1[i]=a[n]
    n+=1
for i in a3: #hfcobahjdsdftv текст
    s1.append(klu1[i])
for i in s: # выводим зашифрованный текст
    print(i,end='')
print()
for i in s1: #d выводим расшифрованный текст
    print (i,end='')




 