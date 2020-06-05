import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from cvxopt import matrix, solvers


def hardlims(n):
    """
    Symmetrical Hard Limit
    """
    if n < 0:
        return -1
    else:
        return 1


class SklearnLinearSVC:
    def __init__(self, X_train, y_train, dual=False, max_iter=1000):
        self.clf = LinearSVC(
            dual=dual, max_iter=max_iter).fit(X_train, y_train)

    def score(self, X_test, y_test):
        return self.clf.score(X_test, y_test)


class SklearnSVC:
    def __init__(self, X_train, y_train, kernel='rbf', gamma='scale', dfs='ovr'):
        self.clf = SVC(kernel=kernel, gamma=gamma,
                       decision_function_shape=dfs).fit(X_train, y_train)

    def score(self, X_test, y_test):
        return self.clf.score(X_test, y_test)


class LinearSVM(object):
    def __init__(self):
        self.func = hardlims

    def fit(self, data_set, labels):
        n, dim = data_set.shape
        P, q = matrix(np.identity(dim+1)), matrix(np.zeros(dim+1))
        G, h = matrix(np.zeros((n, dim+1))), -matrix(np.ones(n))
        P[dim, dim] = 0
        for i in range(n):
            G[i, dim] = float(-labels[i])
            for j in range(dim-1):
                G[i, j] = -labels[i]*data_set[i, j]
        print(P.size, q.size, G.size, h.size)
        sol = solvers.qp(P, q, G, h)
        self.w = np.array(sol['x'][:dim]).reshape(dim)
        self.b = np.array(sol['x'][dim])
        # print("W=", self.w, "\n", "b=", self.b)

    def predict(self, test_set):
        return [(self.func(np.dot(self.w, x)+self.b)) for x in test_set]

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        correct_cnt = sum(y_predict[i] == y_test[i]
                          for i in range(len(y_test)))
        return correct_cnt, correct_cnt/len(y_test)
