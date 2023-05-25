# Очередь с приоритетами
ops = int(input())
btree = []


def sift_up(i_el):
    # Просеивание элемента с индексом i_el вверх к корню
    if i_el == 0:
        return
    i_father = (i_el - 1) // 2
    if btree[i_el] > btree[i_father]:
        btree[i_el], btree[i_father] = btree[i_father], btree[i_el]
        sift_up(i_father)


def sift_down(i_el):
    # Просеивание элемента с индексом i_el вниз
    i_left, i_right = 2 * i_el + 1, 2 * i_el + 2
    if i_left >= len(btree):   # если элемент и так уже внизу, то конец
        return
    guess = i_left
    if i_right < len(btree) and btree[i_right] > btree[i_left]:
        guess = i_right
    if btree[i_el] < btree[guess]:
        btree[i_el], btree[guess] = btree[guess], btree[i_el]
    sift_down(guess)


def insert(p):
    btree.append(p)   # добавили в конец массива
    sift_up(len(btree) - 1)   # просеиваем последний элемент вверх


def extract_max():
    el = btree[0]
    if len(btree) == 1:
        btree.pop()
    else:
        btree[0] = btree.pop()   # положили последний элемент в корень
        sift_down(0)   # просеили его вниз
    return el


for _ in range(ops):
    s = input()
    if s == 'ExtractMax':
        print(extract_max())
    else:
        insert(int(s.lstrip('Insert ')))
 