import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# read CSV
n_features = 5
cuts = 2
data = pd.read_csv(f'./data_{n_features}_{cuts}_cuts.csv')

# get domain and range 
X = data.iloc[:,:-2]
y = data.iloc[:,-2:-1]

# normalize data for speed up convergence
X = (X - X.mean())/X.std()
#   https://stackoverflow.com/questions/52670012/convergencewarning-liblinear-failed-to-converge-increase-the-number-of-iterati

# get datasets for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# SVM 
svm = LinearSVC(dual=False)
svm.fit(X_train, y_train.values.ravel())

predict = svm.predict(X_test)

# render confussion matrix
cm = confusion_matrix(y_test, predict)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm.classes_)
disp.plot()
plt.show()

print(classification_report(y_test, predict))