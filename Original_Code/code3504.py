pdef= 10000
p_var = int(input())
old = 0
a=5000

def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)

s = []
for n in range (20):
  if fib(n) <= 5000 :
    s.append((fib(n)))
    #print(s)

while a != p_var and old <10000:
  old +=1
  if s.count(old) >0:
    a = pdef -old
    pdef = a
  else :
    a = pdef +1
    pdef =a
print (old) 