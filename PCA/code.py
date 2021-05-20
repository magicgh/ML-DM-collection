from scipy.io import loadmat
import numpy as np
import wget


url = 'http://www.cad.zju.edu.cn/home/' +\
        'dengcai/Data/MNIST/2k2k.mat'
dataset = loadmat(wget.download(url))

def ed_pca(data, k):
    n = data.shape[0]
    n_data = (data - data.mean(axis=0))
    cov = np.dot(n_data.T, n_data)/(n - 1)
    val, pc = np.linalg.eig(cov)
    index = np.argsort(val)[::-1][:k]
    return np.dot(n_data, pc[:, index])

def svd_pca(data, k):
    n = data.shape[0]
    n_data = (data - data.mean(axis=0))
    y_data = n_data / np.sqrt(n - 1)
    u, s, vh = np.linalg.svd(y_data)
    return np.dot(n_data, vh[range(k),:].T)

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches


svd_2d = svd_pca(dataset['fea'], 2)
ed_2d = ed_pca(dataset['fea'], 2)

colormap = [list(mcolors.TABLEAU_COLORS)[i]
            for i in range(10)]
            
for i in range(ed_2d.shape[0]):
    x, y = ed_2d[i] # svd_2d[i]
    color = colormap[dataset['gnd'][i][0]]
    plt.scatter(x, y, c=color)
    
handles = [
    mpatches.Patch(color=colormap[i], 
                   label='{}'.format(i))
    for i in range(10)
]

plt.legend(handles=handles, title='Label')
plt.xlabel('First PC')
plt.ylabel('Second PC')

plt.show()