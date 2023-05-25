a = int(input())
strn = (input()).split(' ')
lst = []
for i in strn:
  lst.append (int(i))
cnt = 0
tri = 0
while cnt < a:
    for i in range(a):
      if lst[i] !=  i+1:
        rem_num =lst[i]
        rem_ind = lst.index(i+1)
        lst.insert(i,lst[lst.index(i+1)])
        lst.pop(i+1)
        lst.insert(rem_ind,rem_num)
        lst.pop(rem_ind+1)
        cnt+=1
        tri+=1
      else:
        cnt+=1

print (tri)




 