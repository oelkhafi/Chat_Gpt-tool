def backprop(self, x, y):
    """"""
    Возвращает кортеж ``(nabla_b, nabla_w)`` -- градиент целевой функции по всем параметрам сети.
    ``nabla_b`` и ``nabla_w`` -- послойные списки массивов ndarray,
    такие же, как self.biases и self.weights соответственно.
    """"""

    nabla_b = [np.zeros(b.shape) for b in self.biases]
    nabla_w = [np.zeros(w.shape) for w in self.weights]

    # прямое распространение (forward pass)

    activations = [x]
    sums = [x]
    for b, w in zip(self.biases, self.weights):
        # посчитать активации
        sum = np.dot(w, x)+b
        sums.append(sum)
        x = sigmoid(sum)           
        activations.append(x)
        
    # обратное распространение (backward pass)

    # ошибка выходного слоя
    delta =  self.cost_derivative(activations[-1],y) * sigmoid_prime(sums[-1]) 
        
    # производная J по смещениям выходного слоя
    nabla_b[-1] =  delta
    # производная J по весам выходного слоя
    nabla_w[-1] = np.dot(nabla_b[-1], activations[-2].T)

    # Обратите внимание, что переменная l в цикле ниже используется
    # немного иначе, чем в лекциях.  Здесь l = 1 означает последний слой, 
    # l = 2 - предпоследний и так далее.  
    # Мы перенумеровали схему, чтобы с удобством для себя 
    # использовать тот факт, что в Python к переменной типа list 
    # можно обращаться по негативному индексу.
    for l in range(2, self.num_layers):
       # дополнительные вычисления, чтобы легче записывалось
       #
       # ошибка на слое L-l
       delta = np.dot(self.weights[-l+1].T,nabla_b[-l+1]) * sigmoid_prime(sums[-l]) 
       # производная J по смещениям L-l-го слоя
       nabla_b[-l] = delta 
       # производная J по весам L-l-го слоя
       nabla_w[-l] = np.dot(nabla_b[-l], activations[-l-1].T) 
    return nabla_b, nabla_w 