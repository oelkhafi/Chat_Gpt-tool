import numpy as np

def compute_grad_numerically_2(neuron, X, y, J=J_quadratic, eps=10e-2):
    w_0 = neuron.w
    num_grad = np.zeros(w_0.shape)
    
    for i in range(len(w_0)):
        
        old_wi = neuron.w[i].copy()
        # Меняем вес в одну и другую сторону и считаем целевую функцию
        neuron.w[i] += eps
        J_plus_eps = J(neuron, X, y)
        neuron.w[i] -= 2 * eps
        J_minus_eps = J(neuron, X, y)
        # Вычисляем приближенное значение градиента
        num_grad[i] = (J_plus_eps - J_minus_eps)/(2 * eps)
        
        # Возвращаем вес обратно. Лучше так, чем -= eps, чтобы не накапливать ошибки округления
        neuron.w[i] = old_wi
            
    # проверим, что не испортили нейрону веса своими манипуляциями
    assert np.allclose(neuron.w, w_0), ""МЫ ИСПОРТИЛИ НЕЙРОНУ ВЕСА""
    return num_grad
 