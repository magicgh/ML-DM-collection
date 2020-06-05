from utility import Data, evaluate
import svm_models
import time
if __name__ == "__main__":
    start_time = time.time()
    data = Data()
    data.pca_transform(0.9)
    acc = []
    for X_train, X_test, y_train, y_test in data.load():
        svm = svm_models.SklearnLinearSVC(X_train, y_train)
        acc.append(svm.score(X_test, y_test))
    end_time = time.time()
    evaluate(acc)
    print('total time: %.4fs' % (end_time-start_time))
