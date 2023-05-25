def calc(n):
    arr = [{n}]
    p = 0

    while True:
        curr = set()
        for i,val in enumerate(arr[p]):
            if val % 3 == 0:
                curr.update({val // 3})
            if val % 2 == 0:
                curr.update({val // 2})
            curr.update({val - 1})
            pass
        arr.append((curr))
        p += 1
        if 1 in curr:
            break
        pass

    output = [1]
    for i, current in enumerate(reversed(arr[1:-1])):
        prev = output[i]
        if prev * 3 in current:
            output.append(prev * 3)
            continue
        if prev * 2 in current:
            output.append(prev * 2)
            continue
        if prev + 1 in current:
            output.append(prev + 1)
            continue
        pass
    output.append(n)
    
    print(p)
    print(*output)

    
def main():   
    n = int(input())
    if n == 1:
        print(0, 1, sep = ""\n"")
    else:
        calc(n)


if __name__ == ""__main__"":
    main()
 