n = int(input())
t = [int(i) for i in input().split()]
t1 = t3 = t5 = 0
q1 = q3 = q5 = 0

x = 0
for i in range(0,n):
    x += t[i]
    if x > 300:
        break
    q5 += 1
    t5 += x
#print('Пятикурсник: ',q5,t5)
 
x = 0
for i in range(n-1,-1,-1):
    x += t[i]
    if x > 300:
        break
    q3 += 1
    t3 += x
#print('Третьекурсник: ',q3,t3)

t.sort()
x = 0
for i in range(0,n):
    x += t[i]
    if x > 300:
        break
    q1 += 1
    t1 += x
#print('Первокурсник: ',q1,t1)

st1 = (q1, t1, 1)
st3 = (q3, t3, 3)
st5 = (q5, t5, 5)

st = sorted([st1, st3, st5], reverse=True)

if st[0][0] > st[1][0]:
    print(st[0][2])
else:
    if st[1][0] > st[2][0]:
        st.pop() 
        st.append(st[1])
    st = sorted(st, key=lambda tup: tup[1])
    if st[0][1] < st[1][1]:
        print(st[0][2])
    else:
        if st[1][1] < st[2][1]:
            print(st[1][2])
        else:
            print(st[2][2]) 