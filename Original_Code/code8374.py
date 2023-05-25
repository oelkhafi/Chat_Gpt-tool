# любой узел, в т.ч. корневой:
#     может отличаться от cube
#     может иметь любой цвет
#     может вообще не иметь цвета
import xml.etree.ElementTree

colors = ('red', 'green', 'blue')  # допустимые цвета
weight = {}  # словарь {цвет: вес}
total = []  # список всех узлов уровня 2+ (вложенных в root)

root = xml.etree.ElementTree.fromstring(input())

if root.tag == 'cube' and 'color' in root.attrib:  # если корневой тэг == cube и у него есть цвет
    weight[root.attrib['color']] = weight.get(root.attrib['color'], 0) + 1  # добавим вес цвета в словарь

for color in colors:  # добавляем в список все узлы каждого цвета
    total.extend(root.findall("".//cube[@color='{color}']"".format(color=color)))

level = 2  # уровень, на котором считаем веса цветов
while len(total) > 0:  # будем вести подсчёт повышая уровень, пока не пройдем все элементы
    for color in colors:  # для каждого из цветов
        lst = root.findall(""./{level}[@color='{color}']"".format(color=color, level='cube/' * (level - 1)))  # добавим во временный список узлы c уровня level и цвета color
        weight[color] = weight.get(color, 0) + len(lst) * level  # добавим в словарь вес цвета color
        for el in lst:  # удалим из общего списка узлов посчитанные цвета
            total.remove(el)
    level += 1  # следующий уровень

[print(weight[c], end=' ') for c in colors] 