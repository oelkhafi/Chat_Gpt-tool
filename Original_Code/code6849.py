import json


def finder(ass, find_el, intersection, step=0):
    for i in range(len(ass)):  # ищем наш элемент в начале каждого списка
        if find_el in ass[i][0]:  # если нашли наш элемент, то добавим все грани неповторяющие в наш список
            [intersection.append(element)for element in ass[i] if element not in intersection]
            copy_dic.remove(copy_dic[i])  # удалим вложенный список, чтобы больше на него не тратить время
            step += 1  # увеличиваем наш шаг на один, чтобы больше не искать наш уже найденный элемент
            for find_nod in range(step,len(intersection)):  # перезапускаем функцию, проверяем следующий элемент
                finder(copy_dic, intersection[find_nod], intersection,step)
            return intersection  # возвращаем список предков, который если надо можно использовать
dic, copy_dic, clear_intersection = [], [], []  # создаём пустой список, будующую его копию, список пердков
x = json.loads(input())  # переработаем json-объекты
for y in range(len(x)):
    dic.append([x[y][""name""]])  # берём имя, добавляем его, как вложенный список, где начало = родитель
    for ii in range(len(x)):  # добавим в наш список в правильном порядке всех прямых деток
        if x[y][""name""] in x[ii][""parents""]:  # ищем прямых деток
            dic[y].append(x[ii][""name""])  # присоединяем наших прямых деток
dic = sorted(dic)  # отсортируем список
for parent in dic:  # пробежимся по нашему списку
    copy_dic.clear()  # очистим наш список для копий
    clear_intersection.clear()  # очистим список наших деток
    [copy_dic.append(i) for i in dic]  # копируем наш список
    print(parent[0], "":"", len(finder(copy_dic, parent[0],clear_intersection)))  # родитель скольки деток(включая себя)
 