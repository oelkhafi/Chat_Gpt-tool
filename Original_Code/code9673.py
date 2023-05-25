# put your python code here
from xml.etree import ElementTree

example = input()
rgb_counter = {""red"":0, ""green"":0, ""blue"":0}

root = ElementTree.fromstring(example)  # get root
root_color = root.attrib[""color""]  # get root color
generation = 1
rgb_counter[root_color] = generation  # put root color in dict


def root_recursive(root:ElementTree.Element, generation):
    generation += 1
    for child in root:
        child_color = child.attrib[""color""]
        rgb_counter[child_color] += generation
        root_recursive(child, generation)

root_recursive(root, generation)
print(rgb_counter[""red""], rgb_counter[""green""], rgb_counter[""blue""])
 