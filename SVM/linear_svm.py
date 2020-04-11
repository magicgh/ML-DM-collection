#Implementation on Breast Cancer Dataset
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from cvxopt import matrix, solvers
from transfer_functions import *
# https://github.com/magicgh/machine-learning-homework/blob/master/SVM/transfer_functions.py 
class LinearSVM(object):
    def __init__(self, func):
        self.func=func

    def fit(self, data_set, labels):
        n, dim=data_set.shape
        P, q=matrix(np.identity(dim+1)), matrix(np.zeros(dim+1))
        G, h=matrix(np.zeros((n, dim+1))), -matrix(np.ones(n))
        P[dim, dim]=0
        for i in range(n):
            G[i, dim]=float(-labels[i])
            G[i, :dim]=-labels[i]*data_set[i, :]
        sol=solvers.qp(P, q, G, h)
        self.w=np.array(sol['x'][:dim]).reshape(dim)
        self.b=np.array(sol['x'][dim])
        print("W=", self.w, "\n", "b=", self.b)
    
    def predict(self, test_set):
        return [(self.func(np.dot(self.w,x)+self.b)) for x in test_set]

    def score(self, X_test, y_test):   
        y_predict=self.predict(X_test)
        return sum(y_predict[i]==y_test[i] for i in range(len(y_test)))/len(y_test)

if __name__ == "__main__":
    cancer = datasets.load_breast_cancer()
    for i in range(len(cancer.target)):
        if cancer.target[i]==0:
            cancer.target[i]=-1
    X_train, X_test, y_train, y_test=train_test_split(cancer.data, cancer.target, test_size=0.3)
    clf = LinearSVM(hardlims)
    clf.fit(X_train, y_train)
    print('Accuracy =', clf.score(X_test, y_test))