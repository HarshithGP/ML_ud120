""" 
    Naive Bayes mini-project 

    A Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
import numpy as np
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", round(time()-t0,3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Prediction time: ", round(time()-t1,3), "s"

accuracy = clf.score(features_test, labels_test)
accuracy = accuracy * 100
print "Accuracy = %0.2f"%accuracy,"%"
#print " Accuracy Score =", accuracy_score(pred, labels_test)
