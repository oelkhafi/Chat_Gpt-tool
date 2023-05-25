def front_x(words):
    x_first=[]
    not_x_first=[]
    counter=0
    
    for word in words:
        if len(word)==0:
            continue
        elif word[0]==""x"":
            x_first.append(word)
        else :
            not_x_first.append(word)
            
    counter=words.count("""")
    buf=sorted(x_first)+sorted(not_x_first)
    for _ in range(counter):
        buf.insert(len(x_first),"""")
    return buf

#words = ['x-files', 'xapple', 'xyz', '', 'apple', 'extra', 'mix', """"]
#front_x(words) 