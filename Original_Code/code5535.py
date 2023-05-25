def extend_dictionary(d, key, value):
    if key in d:
        if isinstance(d[key], list):
            d[key].append(value)
        else:
            d[key] = [d[key], value]
    else: d[key] = [value]
       
    return d

def mimic_dict(s):
    s = s.split()
    rez = {"""":[s[0]]}

    for i in range(1,len(s)):
        extend_dictionary(rez, s[i-1], s[i])
    return rez




 