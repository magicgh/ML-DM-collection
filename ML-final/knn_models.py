import numpy as np
import collections
from sklearn.neighbors import KDTree
from sklearn.neighbors import BallTree
import heapq


def gaussian(x, a=1, b=0, c=5):
    return a*np.exp(-(x-b)**2/(2*c**2))


def inv_pp(x, k=1, c=0):
    return k/(x+c)


class kNNClassifier(object):
    def __init__(self, k):
        self.k = k

    def fit(self, dataset, labels):
        self.dataset = dataset
        self.labels = labels

    def predict(self, testset):
        result = []
        for test_data in testset:
            dist = np.array([np.linalg.norm(test_data-v) for v in self.dataset])
            dist_index = np.argsort(dist)[:self.k]
            label_dict = collections.Counter([self.labels[i] for i in dist_index])
            result.append(sorted(label_dict.items(), key=lambda x: x[1], reverse=True)[0][0])
        return result

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return sum(y_predict[i] == y_test[i] for i in range(len(y_test)))/len(y_test)


class Node:
    def __init__(self, data, dim=0, left=None, right=None):
        self.data = data
        self.dim = dim
        self.left = left
        self.right = right


class kNNWithKDTree:

    def __init__(self, k, dataset, label):
        self.dataset = dataset
        self.label = label
        self.k = k
        mod = self.dataset.shape[1]

        def create(data, dim):
            if len(data) == 0:
                return None
            data = sorted(data, key=lambda m: m[dim])
            mid = len(data) // 2
            return Node(data[mid], dim, create(data[:mid], (dim+1) % mod),
                        create(data[mid+1:], (dim+1) % mod))
        self.root = create(self.dataset, 0)

    def query(self, point):
        heap, index, dist = [(-np.inf, None)] * self.k, [], []

        def DFS(node):
            if node is not None:
                dist = point[node.dim] - node.data[node.dim]
                DFS(node.left if dist < 0 else node.right)
                cur_dist = np.linalg.norm(point-node.data)
                heapq.heappushpop(heap, (-cur_dist, node))
                if -(heap[0][0]) > abs(dist):
                    DFS(node.right if dist < 0 else node.left)

        DFS(self.root)
        for ele in heapq.nlargest(self.k, heap):
            index.append(self.dataset.tolist().index(ele[1].data.tolist()))
            dist.append(abs(ele[0]))
        return np.array(dist), np.array(index)

    def predict(self, testset): 
        result = []
        for test_data in testset:
            dist, index = self.query(test_data)
            label_cnt = collections.Counter([self.label[i] for i in index])
            result.append(sorted(label_cnt.items(), key=lambda x: x[1], reverse=True)[0][0])
        return result

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return sum(y_predict[i] == y_test[i] for i in range(len(y_test)))/len(y_test)


class SklearnkNNWithKDTree:
    def __init__(self, k, dataset, label, weighted=None):
        self.dataset = dataset
        self.label = label
        self.k = k
        self.weighted = weighted

    def predict(self, testset):
        tree = KDTree(self.dataset)
        result = []
        for test_data in testset:
            dist, index = tree.query(test_data.reshape(1, -1), self.k)
            if self.weighted is None:
                label_cnt = collections.Counter([self.label[i] for i in index[0]])
            elif self.weighted == 'gaussian':
                label_cnt = {self.label[i]: 0 for i in index[0]}
                for i in range(len(index[0])):
                    label_cnt[self.label[index[0][i]]] += gaussian(dist[0][i])
            elif self.weighted == 'inverse proportional':
                label_cnt = {self.label[i]: 0 for i in index[0]}
                for i in range(len(index[0])):
                    label_cnt[self.label[index[0][i]]] += inv_pp(dist[0][i])
            result.append(sorted(label_cnt.items(), key=lambda x: x[1], reverse=True)[0][0])
        return result

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return sum(y_predict[i] == y_test[i] for i in range(len(y_test)))/len(y_test)


class SklearnkNNWithBallTree:
    def __init__(self, k, dataset, label, weighted=None):
        self.dataset = dataset
        self.label = label
        self.k = k
        self.weighted = weighted

    def predict(self, testset):
        tree = BallTree(self.dataset)
        result = []
        for test_data in testset:
            dist, index = tree.query(test_data.reshape(1, -1), self.k)
            if self.weighted is None:
                label_cnt = collections.Counter([self.label[i] for i in index[0]])
            elif self.weighted == 'gaussian':
                label_cnt = {self.label[i]: 0 for i in index[0]}
                for i in range(len(index[0])):
                    label_cnt[self.label[index[0][i]]] += gaussian(dist[0][i])
            elif self.weighted == 'inverse proportional':
                label_cnt = {self.label[i]: 0 for i in index[0]}
                for i in range(len(index[0])):
                    label_cnt[self.label[index[0][i]]] += inv_pp(dist[0][i])
            result.append(sorted(label_cnt.items(), key=lambda x: x[1], reverse=True)[0][0])
        return result

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return sum(y_predict[i] == y_test[i] for i in range(len(y_test)))/len(y_test)
