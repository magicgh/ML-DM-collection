from utility import Data, evaluate, convert_to_ovr
from svm_models import LinearSVM
import time
if __name__ == "__main__":
    start_time = time.time()
    data = Data()
    acc, correct = [], []
    for X_train, X_test, y_train, y_test in data.load():
        correct_sum, acc_sum = 0, 0
        for z_train, z_test in convert_to_ovr(y_train, y_test):
            clf = LinearSVM()
            clf.fit(X_train, z_train)
            correct_cnt, single_acc = clf.score(X_test, z_test)
            correct_sum += correct_cnt
            acc_sum += single_acc
        acc.append(acc_sum/10)
        correct.append(0.1*correct_sum/len(y_test))
    end_time = time.time()
    print('Overall Accuracy:')
    evaluate(correct)
    print('Average Accuracy:')
    evaluate(acc)
    print('total time: %.4fs' % (end_time-start_time))