def batch_generator(X, y, batch_size=100):
    num_samples = X.shape[0]
    num_batches = int(num_samples / batch_size)
    for i in range(num_batches-1):
        yield X[::batch_size], y[::batch_size]

class LogisticRegressionSGD:
    def __init__(self):
        pass
    
    def __sigmoid(self, h):
        return 1. / (1 + np.exp(-h))

    
    def __extend_X(self, X):
        n, k = X.shape
        X_ext = np.concatenate((np.ones((n, 1)), X), axis=1)
        return X_ext

    def init_weights(self, input_size, output_size):
        np.random.seed(42)
        self.W = np.random.normal(0, 0.01, size=(input_size, output_size))
        
    def get_loss(self, p, y):
        return -(y * np.log(p) + (1 - y) * np.log(1 - p)).mean()
    
    def get_prob(self, X):
        if X.shape[1] != self.W.shape[0]:
            X = self.__extend_X(X)
        return self.__sigmoid(X @ self.W)
    
    def get_acc(self, p, y, threshold=0.5):
        correct = 0
        pred = p >= threshold
        correct = y == pred
        accuracy = (correct.sum()) / len(y)
        return accuracy

    def fit(self, X, y, num_epochs=10, lr=0.001):
        
        X = self.__extend_X(X)
        self.init_weights(X.shape[1], y.shape[1])
        
        accs = []
        losses = []
        for _ in range(num_epochs):
            gen = batch_generator(X, y)
            for X_, y_ in gen:
                p = self.get_prob(X_)

                W_grad = np.dot(X_.T, (p - y_)) / len(y_)
                self.W -= lr * W_grad

                p = np.clip(p, 1e-10, 1 - 1e-10)

                log_loss = self.get_loss(p, y_)
                losses.append(log_loss)
                acc = self.get_acc(p, y_)
                accs.append(acc)
        
        return accs, losses 