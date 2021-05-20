import numpy as np


def download(url, path):
    import wget
    wget.download(url, path)


def download_mnist():
    import os

    if not os.path.exists('./dataset'):
        os.mkdir('./dataset')

    pub_url_head = 'https://ossci-datasets.s3.amazonaws.com/mnist/'
    train_images_url = pub_url_head + 'train-images-idx3-ubyte.gz'
    train_images_path = './dataset/train-images.gz'
    if not os.path.exists(train_images_path):
        download(train_images_url, train_images_path)

    train_labels_url = pub_url_head + 'train-labels-idx1-ubyte.gz'
    train_labels_path = './dataset/train-labels.gz'
    if not os.path.exists(train_labels_path):
        download(train_labels_url, train_labels_path)

    test_images_url = pub_url_head + 't10k-images-idx3-ubyte.gz'
    test_images_path = './dataset/test-images.gz'
    if not os.path.exists(test_images_path):
        download(test_images_url, test_images_path)

    test_labels_url = pub_url_head + 't10k-labels-idx1-ubyte.gz'
    test_labels_path = './dataset/test-labels.gz'
    if not os.path.exists(test_labels_path):
        download(test_labels_url, test_labels_path)
    return train_images_path, train_labels_path, test_images_path, test_labels_path


def dataset_preprocess(train_images_path, train_labels_path, test_images_path, test_labels_path):
    import gzip
    import struct

    train_images = gzip.open(train_images_path, "r")
    train_label = gzip.open(train_labels_path, "r")

    train_images.read(4)
    size, nrows, ncols = struct.unpack(">III", train_images.read(12))

    train_data = np.frombuffer(train_images.read(size * nrows * ncols),
                               dtype=np.dtype(np.uint8).newbyteorder('>')).reshape((size, nrows * ncols))

    train_label.read(8)
    train_label = np.frombuffer(train_label.read(size), dtype=np.dtype(np.uint8).newbyteorder('>'))

    test_images = gzip.open(test_images_path)
    test_label = gzip.open(test_labels_path)

    test_images.read(4)
    test_size = struct.unpack(">I", test_images.read(4))[0]
    test_images.read(8)

    test_data = np.frombuffer(test_images.read(test_size * nrows * ncols),
                              dtype=np.dtype(np.uint8).newbyteorder('>')).reshape((test_size, nrows * ncols))

    test_label.read(8)
    test_label = np.frombuffer(test_label.read(test_size), dtype=np.dtype(np.uint8).newbyteorder('>'))

    return train_data, train_label, test_data, test_label


def small_batch_init(train_data, train_label, test_data, test_label, transformed):
    tr_index = []
    tr_label = []

    for i in range(train_label.shape[0]):
        if train_label[i] == 5:
            tr_index.append(i)
            tr_label.append(1 if transformed else 5)
        elif train_label[i] == 8:
            tr_index.append(i)
            tr_label.append(-1 if transformed else 8)

    te_index = []
    te_label = []

    for i in range(test_label.shape[0]):
        if test_label[i] == 5:
            te_index.append(i)
            te_label.append(1 if transformed else 5)
        elif test_label[i] == 8:
            te_index.append(i)
            te_label.append(-1 if transformed else 8)

    return train_data[tr_index, :], tr_label, test_data[te_index, :], te_label


def mnist_init(batch, transformed=False):
    X1_path, y1_path, X2_path, y2_path = download_mnist()

    X1, y1, X2, y2 = dataset_preprocess(X1_path, y1_path, X2_path, y2_path)
    if batch == 'small':
        return small_batch_init(X1, y1, X2, y2, transformed)

    elif batch == 'complete':
        return X1, y1, X2, y2
    
    elif batch == 'integrated':
        return np.concatenate((X1, X2)), np.concatenate((y1, y2))


def image_peek(data, label=None):
    import matplotlib.pyplot as plt
    data = data.reshape(int(np.sqrt(data.shape[0])), -1)
    plt.figure()

    if not isinstance(label, str):
        plt.imshow(data, cmap='gray', interpolation='none')
        plt.title(f"Ground Truth: {label}")
    else:
        plt.imshow(data, cmap='GnBu', interpolation='none')
        plt.colorbar(cax=None, ax=None)

    plt.xticks([])
    plt.yticks([])
    plt.show()


def proj_peek(data, labels, n):
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import matplotlib.patches as mpatches

    colormap = [list(mcolors.TABLEAU_COLORS)[i] for i in range(n)]

    for i in range(data.shape[0]):
        x, y = data[i]
        color = colormap[labels[i]]
        plt.scatter(x, y, c=color)

    handles = [mpatches.Patch(color=colormap[i], label='{}'.format(i)) for i in range(n)]

    plt.legend(handles=handles, title='Label')
    plt.xlabel('First Axis')
    plt.ylabel('Second Axis')

    plt.show()

def convert2ovr(y_train, y_test):
    for i in range(10):
        yield np.array([1 if x == i else -1 for x in y_train]), np.array([1 if x == i else -1 for x in y_test])

def f1_score(y_true, y_pred):
    from sklearn.metrics import f1_score
    return f1_score(y_true, y_pred, average='macro')

def recall_score(y_true, y_pred):
    from sklearn.metrics import recall_score
    return recall_score(y_true, y_pred, average='macro')
