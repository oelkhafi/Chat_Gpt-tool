def insert(x):
    s.append(x)
    father = len(s) // 2 - 1
    son = len(s) - 1
    while s[father] < s[son] and father >= 0:
        s[father], s[son] = s[son], s[father]  # Меняем местами родителя и добавленный элемент
        son = father
        father = (father + 1) // 2 - 1


def extract_max():
    print(s[0])
    s[0] = s[-1]
    s.pop(-1)
    father, son1, son2 = 0, 1, 2
    while son1 < len(s) and son2 < len(s):  # Пока у узла есть два сына:
        son_max = max(son1, son2, key=lambda x: s[x])
        if s[father] < s[son_max]:
            s[father], s[son_max] = s[son_max], s[father]  # Меняем местами родителя с наибольшим сыном
            father = son_max
            son1 = 2 * father + 1
            son2 = 2 * father + 2
        else:
            break
    if son1 < len(s) <= son2:  # Если у узла только один лист:
        if s[father] < s[son1]:
            s[father], s[son1] = s[son1], s[father]  # Меняем местами родителя и единственный лист


s = []
for i in range(int(input())):
    command = input()
    if command[0] == 'I':
        insert(int(command[7:]))
    else:
        extract_max()
 