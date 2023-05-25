from xml.etree import ElementTree

def calc_colors_of_tree(root, level_cost, rates):
    if root is None:
        return rates
    rates[root.attrib['color']] += level_cost
    for el in root:
        rates = calc_colors_of_tree(el, level_cost+1, rates)
        
    return rates


def calc_colors(s):
    names = ['red', 'green', 'blue']
    rates = {x:0 for x in names}
    root = ElementTree.fromstring(s)
    rates = calc_colors_of_tree(root, 1, rates)
    return [rates[x] for x in names]


print("" "".join(map(str, calc_colors(input()))))
     