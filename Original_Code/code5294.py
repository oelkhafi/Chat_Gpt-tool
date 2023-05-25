n,i = int(input()),2
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i:
            continue
        else:
            return False
    return True
while n>1:
    if n%i == 0:
        print(i, end=' ')
        d = n//i
        if prime(d):
            print(d, end=' ')
            break
        n = d
        i = 2
        continue
    i+=1 