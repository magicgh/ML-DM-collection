#Implementation on Handwriting Digits Dataset
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm

if __name__ == "__main__":
    digits = datasets.load_digits()
    X_train, X_test, y_train, y_test=train_test_split(digits.data, digits.target, test_size=0.3)
    clf = svm.SVC(decision_function_shape='ovr').fit(X_train, y_train)
    print(clf.score(X_test, y_test))
   
    