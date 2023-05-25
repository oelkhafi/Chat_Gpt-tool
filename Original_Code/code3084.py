def check(pole, width, height):
    #обход всех точек поля и печать расстановки для 2 поколения
    alive = 0
    for row in range(height):  # ограничение точек перебора в высоту
        for col in range(width):  # ограничение точек перебора в ширину
            for j in [-1, 0, 1]:  # шаг движения по строкам
                for k in [-1, 0, 1]:  # шаг движения по столбцам
                        X = row + j if row + j < height else 0
                        Y = col + k if col + k < width else 0
                        alive += pole[X][Y].count(""X"")
                
            if pole[row][col] is ""."":
                print(""X"" if alive == 3 else ""."", end="""")
            elif pole[row][col] is ""X"":
                print(""X"" if 3 <= alive <= 4 else ""."", end="""")
            alive = 0
        print()
    return 

def main():
    height, width = map(int, input().split())
    pole = [[i for i in input()] for j in range(height)]

    check(pole, width, height)
    
if __name__ == ""__main__"":
    main()
     