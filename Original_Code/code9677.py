def kaprekar(n):
    sq = n**2
    l_sq = numerics(sq)
    for i in range(len(l_sq)):
        left = l_sq[0:i]
        right = l_sq[i:len(l_sq)]
        left = ''.join([str(x) for x in left])
        right = ''.join([str(x) for x in right])
        try:
            left = int(left)
        except ValueError as e:
            continue
        else:
            if left == 0: continue
        try:
            right = int(right)
        except ValueError as e:
            continue
        else:
            if right == 0: continue
        if left + right == n:
            return True
    return False

def numerics(n):
    s = str(n)
    return [int(x) for x in s] 