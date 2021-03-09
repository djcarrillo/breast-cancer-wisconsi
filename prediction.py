import os
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np



#class PREDICTIONS:

    #def __init__(self):

def predictions(patient):

    classifier = GaussianNB()

    source = pd.read_csv('my_first_server/breast-cancer-wisconsin_1.csv')

    source.columns = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
                      'Uniformity of Cell Shape',
                      'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                      'Normal Nucleoli', 'Mitoses', 'Class']

    source.dropna(how='all')

    x_train, x_test, y_train, y_test = train_test_split(source.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].values,
                                                        source['Class'].values, test_size=0.3, random_state=0)

    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)

    cm = confusion_matrix(y_test, y_pred)

    print(cm)

    y_pred = classifier.predict(np.array(patient))

    print(y_pred)

    return y_pred

    #def predictions_(self):
    #    a = np.array([[1000025, 5, 1, 1, 1, 2, 1, 3, 2]])
    #    y_pred = self.classifier(a)|
        #return 1

