# put your python code here
s = input()
a = input()
b = input()
if s.find(a) == -1:
    print(0)
else:
    new = s.replace(a, b)
    k = 1
    while a in new:
        new = new.replace(a,b)
        k += 1
        if k > 1000:
            print(""Impossible"")
            break
    if k < 1000:
        print(k)




 