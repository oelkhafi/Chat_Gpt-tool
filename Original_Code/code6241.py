a,n,i,j=0,int(input()),0,0
l=[[0 for w in range(n)] for h in range(n)]
while a<n**2:
    a+=1
    l[i][j]=a
    if 0<=j-1<n and l[i][j-1]==0 and 0<=i-1<n and l[i-1][j]==0:
        j-=1
    elif 0<=i-1<n and l[i-1][j]==0 and 0<=j+1<n and l[i][j+1]==0:
        i-=1
    elif 0<=j+1<n and l[i][j+1]==0:
        j+=1
    elif 0<=i+1<n and l[i+1][j]==0:
        i+=1
    elif 0<=j-1<n and l[i][j-1]==0:
        j-=1
    elif 0<=i-1<n and l[i-1][j]==0:
        i-=1
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print() if i!=l else '' 