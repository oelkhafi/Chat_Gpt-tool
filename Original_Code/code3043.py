from xml.etree import ElementTree as ET


root = ET.fromstring(input())
dict = dict(red=0, blue=0, green=0)
dict[root.attrib[""color""]] = 1
value = 2

def func(root, value):
    for child in root:
        key = child.attrib[""color""]
        dict[key] += value
        if len(child) > 0:
            func(root=child, value=value+1)
        else:
            continue

for child in root:
    key = child.attrib[""color""]
    dict[key] += value
    if len(child) > 0:
        func(root=child, value=value+1)
    else: continue

print(dict['red'], dict['green'], dict['blue'])
 