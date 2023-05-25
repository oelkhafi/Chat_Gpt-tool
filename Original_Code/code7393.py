from xml.etree import ElementTree


def runner(level, color, parent_element):
    global r, g, b
    if color == 'red':
        r += level
    elif color == 'green':
        g += level
    elif color == 'blue':
        b += level
    for element in parent_element:
        runner(level+1, element.attrib['color'], element)


r, g, b = 0, 0, 0
root = ElementTree.fromstring(input())
runner(1, root.attrib['color'], root)

print(r, g, b)
 