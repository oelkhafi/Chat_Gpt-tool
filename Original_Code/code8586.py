class Buffer():
    def __init__(self):
        """"""Инициирует буфер""""""
        self.buff = []

    def add(self, *a):
        """"""
            добавить следующую часть последовательности и выводит
            сумму пятёрок
        """"""
        for i in a:
            self.buff.append(i)
            if len(self.buff) == 5:
                print(sum(self.buff))
                self.buff = []
    def get_current_part(self):
        """"""
            вернуть сохраненные в текущий момент элементы 
            последовательности в порядке, в котором они были добавлены
        """"""
        return self.buff 