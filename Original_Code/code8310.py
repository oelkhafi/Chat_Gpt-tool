from xml.etree import ElementTree

cube = {'red': 0, 'green': 0, 'blue': 0}

tree = ElementTree.fromstring(input())
cube[tree.attrib['color']] += 1


def ok(root, lvl=1):
    global cube
    for element in root:
        cube[element.attrib['color']] += lvl + 1
        ok(element, lvl=lvl + 1)


ok(tree)
print(*cube.values())



 