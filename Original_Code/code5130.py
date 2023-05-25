def create_matrix(size):
    return [None for _ in range(size * size)]


def add_element(element, matrix):
    # если добавляемый элемент - None, возвращаем матрицу
    if element is None:
        return matrix
    # узнаем индекс первого ""нулевого"" элемента
    idx = matrix.index(None)
    # добавляем элемент
    matrix[idx] = element
    # определяем размер матрицы
    size = int(len(matrix) ** 0.5)
    # проверяем нужно ли увеличивать размер матрицы
    if idx == size * (size - 1):
        # увеличиваем размер матрицы
        matrix.extend([None, ] * ((size + 1) ** 2 - len(matrix)))
    # возвращаем матрицу
    return matrix


def matrix_to_string(matrix):
    result = ''
    size = int(len(matrix) ** 0.5)
    for row in range(size):
        result += ' '.join([str(i) for i in matrix[size * row:size * (row + 1)]]) + '\n'
    return result 