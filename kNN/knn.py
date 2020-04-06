import numpy as np
import collections 
from sklearn.model_selection import train_test_split
from sklearn import datasets

class kNNClassifier(object):
    def __init__(self, k_value):
        self.k=k_value
    
    def fit(self, data_set, labels):
        self.data_set=data_set
        self.labels=labels

    def predict(self, test_set):
        result=[]
        for test_data in test_set:
            dist=np.array([np.linalg.norm(test_data-v) for v in self.data_set])
            dist_index=np.argsort(dist)[:self.k]
            label_dict=collections.Counter([self.labels[i] for i in dist_index])
            result.append(sorted(label_dict.items(),key=lambda x:x[1],reverse=True)[0][0])
        return result

    def score(self, X_test, y_test):   
        y_predict=self.predict(X_test)
        return sum(y_predict[i]==y_test[i] for i in range(len(y_test)))/len(y_test)

if __name__ == "__main__":
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test=train_test_split(iris.data, iris.target, test_size=0.3)
    knn = kNNClassifier(5)
    knn.fit(X_train, y_train)
    print('Accuracy =',knn.score(X_test, y_test))