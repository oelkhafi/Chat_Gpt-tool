def sort_cw(i):
    return i[0]/i[1]
n,W=map(int,input().split())
W_sum=float()
summ=float()
tov=[]
for i in range(n):
    c,w=map(int,input().split())
    tov.append([c,w])
tov.sort(key=sort_cw)
tov.reverse()
for i in range(len(tov)):
    W_sum+=tov[i][1]
    summ+=tov[i][0]
    if W_sum>W:
        W_sum=W_sum-tov[i][1]
        summ=summ-tov[i][0]
        summ=summ+tov[i][0]*(W-W_sum)/tov[i][1]
        break
print(""%.3f"" % summ)




 