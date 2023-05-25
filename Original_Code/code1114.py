# convert from unit to meters
scales = {
'mile': 1609, 
'yard': 0.9144, 
'foot': 0.3048, 
'inch': 0.0254, 
'km': 1000, 
'm': 1,
'cm': 0.01,
'mm': 0.001 }


# val - float - number to convert
# fr - a name of the unit to convert from
# to - a name of the unit to convert to
def convert(fr, to, val):
    if val == 0:
        return 0
    fromK = scales[fr]
    toK = scales[to]
    if fromK is None or toK is None:
        return val
    return (val * fromK) / toK
 

s = input().split()
print(""{:.2e}"".format(convert(s[1], s[3], float(s[0]))))
 