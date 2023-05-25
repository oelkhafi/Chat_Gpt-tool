from xml.etree import ElementTree

colors = {'red': 0, 'green': 0, 'blue': 0}

root = ElementTree.fromstring(input())

for color in colors:
    if color == root.attrib['color']:
        colors[color] = 1

def get_value(root, color, depth):
    for child in root:
        if child.attrib['color'] == color:
            colors[color] += depth
        if len(child) != 0:
            get_value(child, color, depth + 1)

get_value(root, 'red', 2)
get_value(root, 'green', 2)
get_value(root, 'blue', 2)

print(colors['red'], colors['green'], colors['blue'])

 