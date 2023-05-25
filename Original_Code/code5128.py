
class Matrix:
    MAX_SIZE = 1000  # максимальное допустимое количество строк

    def __init__(self, max_size=None):
        self.max_size = max_size or self.MAX_SIZE
        self.current_size = 1
        self.matrix = [None, ]
        self.null_idx = 0
        self.resize_up_idx = 0
        self.resize_down_idx = 0

    def append(self, element=None):
        # если element=None, не добавляем
        if element is None:
            return
        # проверяем нужно ли увеличивать размер матрицы
        if self.null_idx == self.resize_up_idx:
            # увеличиваем размер матрицы
            self.resize_up()
        # добавляем элемент в матрицу
        self.matrix[self.null_idx] = element
        # изменяем текущий индекс нулевого элемента
        self.null_idx += 1

    def resize_up(self):
        # проверяем: текущий размер матрицы максимально допустимый?
        if self.current_size == self.max_size:
            # не изменяем размер матрицы
            return
        # увеличиваем текущий размер матрицы
        self.current_size += 1
        # расширяем саму матрицу
        self.matrix.extend([None, ] * (self.current_size ** 2 - len(self.matrix)))
        # изменяем значения атрибутов resize_down_idx и resize_up_idx
        self.resize_down_idx = (self.current_size - 1) * (self.current_size - 2)
        self.resize_up_idx = self.current_size * (self.current_size - 1)

    def pop(self):
        # если матрица 'пустая' выкидываем IndexError
        if self.current_size == 1 and self.matrix[0] is None:
            raise IndexError
        # проверяем нужно ли уменьшать размер матрицы
        if self.null_idx - 1 == self.resize_down_idx:
            # уменьшаем размер матрицы
            self.resize_down()
        # извлекаем элемент, устанавливаем него место None
        result, self.matrix[self.null_idx - 1] = self.matrix[self.null_idx - 1], None
        # иизменяем текущий индекс нулевого элемента
        self.null_idx -= 1
        # возвращаем элемент
        return result

    def resize_down(self):
        # уменьшаем текущий размер матрицы
        self.current_size -= 1
        # обрезаем матрицу по новому размеру
        self.matrix = self.matrix[:self.current_size ** 2]
        # устанавливаем новое значение атрибута resize_up_idx
        # self.resize_up_idx = self.resize_down_idx + 1
        self.resize_up_idx = self.current_size * (self.current_size - 1)
        # вычисляем новое значение атрибута resize_down_idx
        self.resize_down_idx = (self.current_size - 1) * (self.current_size - 2)

    def __str__(self):
        output = ''
        for row in range(self.current_size):
            start = self.current_size * row
            end = self.current_size * (row + 1)
            output += ' '.join([str(i) for i in self.matrix[start:end]]) + '\n'
        return output

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        matrix = cls(max_size)

        for element in iter_obj:
            matrix.append(element)

        return matrix 