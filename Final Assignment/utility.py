import scipy.io as sio
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler


class Data:
    def __init__(self):
        self.data_set = sio.loadmat('mnist.mat')
        self.data_index = sio.loadmat('index.mat')
        self.data = self.data_set['data']
        self.label = self.data_set['label']
        self.train_index = self.data_index['train_index']
        self.test_index = self.data_index['test_index']

    def pca_transform(self, n_components=0.8):
        pca = PCA(n_components)
        self.data = pca.fit_transform(self.data)

    def lda_transform(self, solver='svd', n_components=None):
        lda = LinearDiscriminantAnalysis(
            solver=solver, n_components=n_components)
        self.data = lda.fit_transform(self.data, self.label.flatten())

    def stardard_transform(self):
        stardard = StandardScaler()
        self.data = stardard.fit_transform(self.data)

    def load(self):
        for i in range(5):
            yield np.array([self.data[j] for j in self.train_index[i]]),\
                np.array([self.data[j] for j in self.test_index[i]]),\
                np.array([self.label[0][j] for j in self.train_index[i]]),\
                np.array([self.label[0][j] for j in self.test_index[i]])


def evaluate(acc):
    print('mean=%.4f%%, std=%.8f' % (np.mean(acc)*100, np.std(acc)))


def convert_to_ovr(y_train, y_test):
    for i in range(10):
        yield np.array([1 if x == i else -1 for x in y_train]),\
            np.array([1 if x == i else -1 for x in y_test])
