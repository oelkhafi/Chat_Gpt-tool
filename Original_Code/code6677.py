n=int(input())
m=[[0 for j in range(n)] for i in range(n)]

def frame(start,length,m,counter):
  for i in range(start, start+length):
    counter+=1
    m[start][i]=counter
  for i in range(start+1,start+length):
    counter+=1
    m[i][length-1+start]=counter
  
  for i in range(length+start-1,start,-1):
    counter+=1
    m[start+length-1][i-1]=counter
  for i in range (length+start-2,start,-1):
    counter+=1
    m[i][start]=counter
  return counter, m

k=n # lenght of the row
j=0 # row's number
counter=0

while True:
  counter,m = frame(j,k,m,counter)
  j+=1
  k-=2
  if n==1 or m[j][j]!=0: break

for l in m:
  for w in l:
    print (w, end=""\t"")
  print () 