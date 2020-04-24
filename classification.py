import numpy as np
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def predict_perceptron(a,b):
    k=[]
    for t in range(len(last_list)):
        y = ['n']*last_list[t][a].shape[0] + ['m']*last_list[t][b].shape[0]
        X = np.concatenate((last_list[t][a],last_list[t][b]),axis=0)
        ppn = Perceptron(tol=1e-3, random_state=0)
        s=[]
        for i in range(10):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
            ppn.fit(X_train, y_train)
            y_pred = ppn.predict(X_test)
            m=accuracy_score(y_test, y_pred)
            s.append(m)
        m1=s.mean()
        k.append(m1)
    return k
def predict_svm(a,b):
    k=[]
    for t in range(len(last_list)):
        y = ['n']*last_list[t][a].shape[0] + ['m']*last_list[t][b].shape[0]
        X = np.concatenate((last_list[t][a],last_list[t][b]),axis=0)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        svm.fit(X_train, y_train)
        y_pred = .predict(X_test)
        m=accuracy_score(y_test, y_pred)
        k.append(m)
    return k