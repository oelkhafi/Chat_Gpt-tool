def sigmoid(h):
        return 1. / (1 + np.exp(-h))
class LogisticRegressionGD:

    def __init__(self):
        pass
    
    def __extend_X(self, X):
        n, k = X.shape
        X_ext = np.concatenate((np.ones((n, 1)), X), axis=1)
        return X_ext

    #def sigmoid(h):
        #return 1. / (1 + np.exp(-h))

    def init_weights(self, input_size, output_size):
        np.random.seed(42)
        self.W = np.random.normal(0, 0.01, size=(input_size, output_size))
        
    def get_loss(self, p, y):   
        return np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    
    def get_prob(self, X):
        if X.shape[1] != self.W.shape[0]:
            X = self.__extend_X(X)
        return sigmoid(X @ self.W)
    
    def get_acc(self, p, y, threshold=0.5):
        correct = 0
        pred = p >= threshold
        correct = y == pred
        accuracy = (correct.sum()) / len(y)
        return accuracy

    def fit(self, X, y, num_epochs=100, lr=0.001):
        
        X = self.__extend_X(X)
        self.init_weights(X.shape[1], y.shape[1])
        
        accs = []
        losses = []
        for _ in range(num_epochs):
            p = self.get_prob(X)

            W_grad = np.dot(X.T, (p - y)) / len(y)
            self.W -= lr * W_grad
            
            p = np.clip(p, 1e-10, 1 - 1e-10)
            
            log_loss = self.get_loss(p, y)
            losses.append(-log_loss)
            acc = self.get_acc(p, y)
            accs.append(acc)
        
        return accs, losses
 