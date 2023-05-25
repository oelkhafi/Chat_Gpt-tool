def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            l[i] = 'K'
            i += 1
            if i >= len(l):
                break
        if l[i] % 2 == 0:
            l[i] = int(l[i] // 2)
            i += 1
            if i >= len(l):
                break
    if 'K' in l:
        if l.count('K') == len(l):
            l.clear()
        else:
            while True:
                l.remove('K')
                if 'K' not in l:
                    break 