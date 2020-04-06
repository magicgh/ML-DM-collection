import numpy as np
from transfer_functions import *
class Perceptron(object):
    def __init__(self, W, b):
        self.Weights = W
        self.bias = b
        self.transfer_function = np.vectorize(hardlims)
    def classify(self, prototype):
        net_input = self.Weights.dot(prototype) + self.bias
        return self.transfer_function(net_input)
W = np.array([0.5, 0])
b = -0.75
if __name__ == "__main__":
    p1 = np.array([1, 0.5]).reshape((2, 1))
    p2 = np.array([2, 1]).reshape((2, 1))
    test = Perceptron(W,b)
    print(test.classify(p1)) #except -1
    print(test.classify(p2)) #except 1
    #extra test
    p3 = np.array([1, 1]).reshape((2, 1))
    p4 = np.array([2, 0]).reshape((2, 1))
    print(test.classify(p3)) #except -1
    print(test.classify(p4)) #except 1