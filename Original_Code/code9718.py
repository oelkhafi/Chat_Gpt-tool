items_not_mod3 = []
items_mod3 = []

while True:
    num = int(input())
    if num == 0:
        break

    if num % 3 == 0:
        items_mod3.append(num)
    else:
        items_not_mod3.append(num)

total_items_not_mod3 = len(items_not_mod3)
total_items_mod3 = len(items_mod3)

total_even = len([x for x in items_mod3 if x % 2 == 0])
total_odd = len([x for x in items_not_mod3 if x % 2 == 1])

print(round(total_even / total_items_mod3 * 100))
print(round(total_odd / total_items_not_mod3 * 100)) 