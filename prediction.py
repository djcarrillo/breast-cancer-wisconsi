import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np


class PREDICTIONS:

    def __init__(self):
        self.classifier = GaussianNB()

        source = pd.read_csv('my_first_server/breast-cancer-wisconsin_1.csv')

        source.columns = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
                          'Uniformity of Cell Shape',
                          'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                          'Normal Nucleoli', 'Mitoses', 'Class']

        source.dropna(how='all')

        x_train, x_test, y_train, y_test = train_test_split(source.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].values,
                                                            source['Class'].values, test_size=0.3, random_state=0)

        self.classifier.fit(x_train, y_train)

        y_pred = self.classifier.predict(x_test)

        cm = confusion_matrix(y_test, y_pred)

        print("Matriz de confusión:", cm)

        # y_pred = self.classifier.predict(np.array(patient))

        # print(y_pred)

        # return self.classifier


clase = PREDICTIONS()


def predictions_(patient):
    return clase.classifier.predict(np.array(patient))
