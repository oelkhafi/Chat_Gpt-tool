from copy import copy,deepcopy
spisok=[]
spisok2=[]
stop=['end']
while stop not in spisok:
  spisok+=[list(input().split())]
spisok.pop()
cnt = (len(spisok))
cnt1 = (len(spisok[0]))
spisok2 =deepcopy(spisok)
if cnt==1 and cnt1==1:
  for i in range (0,-cnt,-1):
    for j in range (0,-cnt1,-1):
      spisok2[i][j]=int(spisok[i-1][j-1]) + int(spisok[i-1][j]) + int(spisok[i][j-1]) + int(spisok[i][j])
elif cnt1 >=1 and cnt <=1:
  for i in range (0,-cnt,-1):
    for j in range (0,-cnt1,-1):
      spisok2[i][j]=int(spisok[i][j]) + int(spisok[i-1][j+1]) + int(spisok[i][j-1]) + int(spisok[i][j])
elif cnt1 <=1 and cnt >=1:
  for i in range (0,-cnt,-1):
    for j in range (0,-cnt1,-1):
      spisok2[i][j]=int(spisok[i][j]) + int(spisok[i+1][j]) + int(spisok[i-1][j]) + int(spisok[i][j-1])
else:
  for i in range (0,-cnt,-1):
    for j in range (0,-cnt1,-1):
      spisok2[i][j]=int(spisok[i-1][j]) + int(spisok[i+1][j]) + int(spisok[i][j-1]) + int(spisok[i][j+1])
for zi in range (cnt):
  for zj in range (cnt1):
    #print(''.join(spisok2[zi][zj]),sep='***', end='')
    print(spisok2[zi][zj],' ',end ='')
  print() 