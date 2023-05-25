def backprop(self, x, y):
    """"""
    Возвращает кортеж ``(nabla_b, nabla_w)`` -- градиент целевой функции по всем параметрам сети.
    ``nabla_b`` и ``nabla_w`` -- послойные списки массивов ndarray,
    такие же, как self.biases и self.weights соответственно.
    """"""

    nabla_b = [np.zeros(b.shape) for b in self.biases]
    nabla_w = [np.zeros(w.shape) for w in self.weights]

    # прямое распространение (forward pass)
    a = [x] # список векторов активаций
    for b, w in zip(self.biases, self.weights):
        # посчитать активации
        a.append(sigmoid(np.dot(w, a[-1]) + b))

    # обратное распространение (backward pass)
    delta = (a[-1] - y)*(a[-1] - a[-1]**2)  # ошибка выходного слоя
    nabla_b[-1] = delta  # производная J по смещениям выходного слоя
    nabla_w[-1] = delta.dot(a[-2].T)  # производная J по весам выходного слоя
        
    # Обратите внимание, что переменная l в цикле ниже используется
    # немного иначе, чем в лекциях.  Здесь l = 1 означает последний слой, 
    # l = 2 - предпоследний и так далее.  
    # Мы перенумеровали схему, чтобы с удобством для себя 
    # использовать тот факт, что в Python к переменной типа list 
    # можно обращаться по негативному индексу.
    for l in range(2, self.num_layers):
        # дополнительные вычисления, чтобы легче записывалось
        #
        delta = self.weights[-l + 1].T.dot(delta) * (a[-l] - a[-l]**2) # ошибка на слое L-l
        nabla_b[-l] = delta # производная J по смещениям L-l-го слоя
        nabla_w[-l] = delta.dot(a[-l - 1].T) # производная J по весам L-l-го слоя
    return nabla_b, nabla_w 