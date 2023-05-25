# put your python code here
from xml.etree import ElementTree

def recurcionForCubes(el, root, value):
    value += 1
    dict_value[el.attrib['color']] += [value]
    for child in el:
        if child in el:
            recurcionForCubes(child, el, value)
            
root = ElementTree.fromstring(input())

dict_value = {'red':[0], 'green':[0], 'blue':[0]}
dict_value[root.attrib['color']] += [1]

for el in root:
    value = 1
    recurcionForCubes(el, root, value)
print('{} {} {}'.format(sum(dict_value['red']), sum(dict_value['green']), sum(dict_value['blue'])))



 