num_1 = int(input())
meadow = ""На лугу""
cow_1 = ""корова""
cow_2 = ""коров""
cow_3 = ""коровы""
for i in range(1, num_1+1):
    if i < 20:
        if i == 1:
            print(meadow, i, cow_1)
        elif i == 2 or i == 3 or i == 4:
            print(meadow, i, cow_3)
        else:
            print(meadow, i, cow_2)
    else:
        if i%10 == 1:
            print(meadow, i, cow_1)
        elif i%10 == 2 or i%10 == 3 or i%10 == 4:
            print(meadow, i, cow_3)
        else:
            print(meadow, i, cow_2)




 