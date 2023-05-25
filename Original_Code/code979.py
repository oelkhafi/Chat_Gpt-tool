# put your python code here
def main():
    seq = []
    n = int(input())
    while n:
        seq.append(n)
        n = int(input())
    print(min_distance(localmaxs(seq)))

def localmaxs(lst):
    locmaxindxs = []
    maybe = False
    if len(lst) < 3: return []
    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1]: maybe = True
        elif lst[i] > lst[i+1]:
            if maybe: locmaxindxs.append(i)
            maybe = False
    return locmaxindxs

def min_distance(lst):
    if len(lst) >= 2:
        dst = abs(lst[1] - lst[0])
        for i in range(1, len(lst)-1):
            dst = min(dst, abs(lst[i+1] - lst[i]))
    else: dst = 0
    return dst
                 
if __name__ == ""__main__"": main() 