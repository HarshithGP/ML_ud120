#!/usr/bin/python

""" 
   Support Vector Machine mini-project.

    A SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

from sklearn.svm import SVC
clf = SVC(kernel="rbf",C=10000.0)

t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", round(time()-t0,3), "s"

t1 = time() 
pred = clf.predict(features_test)
print "Prediction time: ", round(time()-t1,3), "s"

accuracy = clf.score(features_test, labels_test)*100
print "Accuracy = %0.2f"%accuracy

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)*100
print "Accuracy Score = %0.2f"%acc

ctr=0
for i in range(0,len(pred)):
	if pred[i]==1 :
		ctr=ctr+1
print "No of emails by Chris =",ctr
print "No of emails by Sara =", len(pred)-ctr 

