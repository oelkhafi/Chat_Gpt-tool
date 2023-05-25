def find_j(j, l, r, i, A):
    while l <= r:
        if A[j] == i:
            return j + 1
        else:
            if A[j] > i:
                r = j - 1
            else:
                l = j + 1
            j = (l + r) // 2
    else: return -1


def main():
    A = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    n, k = A.pop(0), b.pop(0)
    
    l, r = 0, n - 1
    j = (l + r) // 2
    
    for i in b:
        print(find_j(j, l, r, i, A), end="" "")
        
        
if __name__ == ""__main__"":
    main()
     