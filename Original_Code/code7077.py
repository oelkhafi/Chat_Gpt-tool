data = input().split()

volume = int(2 * float(data[0]))  # нужный объём умножаем на 2 для удобства
price = list(map(int, data[1:]))  # список стоимостей

VESSEL = [1, 2, 3, 4]  # список доступных объёмов (уже умноженных на 2)
COUNT = 4
value = [p / v for (p, v) in zip(price, VESSEL)]  # ценность каждого товара, денег/литр

solution = [0, 0, 0, 0]  # это будет решение по товарам
index = value.index(min(value))  # находим товар с минимальной ценностью
solution[index] = volume // VESSEL[index]  # почти очевидно, что максимум нужного объёма получится из найденного товара
rest = volume % VESSEL[index]  # считаем остаток, который надо докупить

# остаток добирается ВСЕГДА только одним товаром, это можно доказать строго (для данной задачи)
# посчитаем, сколько единиц каждого товара надо, чтобы купить нужный объём, но считаем сразу в стоимости
rest_costs = [price[i] * int((rest + VESSEL[i] - 0.1) / VESSEL[i]) for i in range(COUNT)]
min_cost = min(rest_costs)  # находим минимальную стоимость
min_cost_index = rest_costs.index(min_cost)  # находим, на какой позиции находится минимальная стоимость
solution[min_cost_index] += int(rest_costs[min_cost_index] / price[min_cost_index])  # дополняем решение
# print(*solution)  # если надо посмотреть решение - достаточно раскомментировать
print(sum(solution[i] * price[i] for i in range(COUNT)))  # а вот и искомый результат
 