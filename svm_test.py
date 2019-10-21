import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

#example dataset
#x = [1, 5, 1.5, 8, 1, 9]
#y = [2, 8, 1.8, 8, 0.6, 11]

#load breast cancer dataset
cancer = datasets.load_breast_cancer()

#print("Features: ", cancer.feature_names)
#print("Labels: ", cancer.target_names) #malignant or benign

#print (cancer.data.shape)

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109) #70% training 30% test

#new SVM classifer
clf = svm.SVC(kernel='linear')

#train model using training sets
clf.fit(X_train, y_train)

#predict response for test dataset
y_pred = clf.predict(X_test)

#model accuracy, how often is the classifer correct
print("Accuracy: ",metrics.accuracy_score(y_test, y_pred))

#model precision, percentage of positive tuples labeled as such
print("Precision: ",metrics.precision_score(y_test, y_pred))

#model recall, idk what this is
print("Recall: ",metrics.recall_score(y_test, y_pred))



