# put your python code here
from xml.etree import ElementTree

def countColors(root, a):
    a+=1
    for c in root:      
        if c.attrib['color'] in colors:
            colors[c.attrib['color']]+=a
        else:
            continue
        countColors(c, a)

colors = {'red':0, 'green':0, 'blue':0}

str_xml = input()
root = ElementTree.fromstring(str_xml)

if root.attrib['color'] in colors:
    colors[root.attrib['color']]+=1

for element in root:
    a = 2
    colors[element.attrib['color']]+=a
    countColors(element, a = 2)
    
print(colors['red'], colors['green'],colors['blue']) 