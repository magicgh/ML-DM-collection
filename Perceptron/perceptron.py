#Implementation on Breast Cancer Dataset
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from transfer_functions import * 
class Perceptron(object):
    def __init__(self, max_iter, lr, func):
        self.max_iter=max_iter
        self.lr=lr
        self.func=func

    def fit(self, data_set, labels):
        self.data_set=data_set
        self.labels=labels
        self.w=np.zeros(data_set.shape[1])
        self.b=0
        for i in range(self.max_iter):
            flag=0
            for x,y in zip(data_set, labels):
                y_=self.func(np.dot(self.w,x)+self.b)
                if y!=y_:
                    self.w+=(y-y_)*self.lr*x
                    self.b+=(y-y_)*self.lr
                    flag=1
            if flag==0:
                break
        print("W=", self.w, "\n", "b=", self.b)

    
    def predict(self, test_set):
        return [self.func(np.dot(self.w,x)+self.b) for x in test_set]

    def score(self, X_test, y_test):   
        y_predict=self.predict(X_test)
        return sum(y_predict[i]==y_test[i] for i in range(len(y_test)))/len(y_test)

if __name__ == "__main__":
    cancer = datasets.load_breast_cancer()
    X_train, X_test, y_train, y_test=train_test_split(cancer.data, cancer.target, test_size=0.3)
    clf = Perceptron(100, 0.01, hardlim)
    clf.fit(X_train, y_train)
    print('Accuracy =', clf.score(X_test, y_test))