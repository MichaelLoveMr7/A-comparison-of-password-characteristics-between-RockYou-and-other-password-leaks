# -*- coding: utf-8 -*-
"""
Modified Sept 2019

@author: mvm for INFR3700/MITS6800 following Geron's
"""

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import confusion_matrix
import pandas as pd
pswd_data = pd.read_csv(r'/Users/yujiedong/Downloads/BreachCompilation/data/random_1.3Billion.csv')
print(pswd_data)
# Add column for classification. True if >=100; False otherwise


# Create training/testing datasets
from sklearn.model_selection import train_test_split
train, test = train_test_split(pswd_data, test_size=0.2, random_state=42)
train_labels = train.loc[train.iloc[:,2]>-1].iloc[:,2]
train_data = train.loc[train.iloc[:,1]>-1].iloc[:,1]
test_labels = test.loc[test.iloc[:,2] > -1].iloc[:,2]
test_data = test.loc[test.iloc[:,1] > -1].iloc[:,1]
import numpy as np
x = np.c_[train_data]
y = np.c_[train_labels]
x_test = np.c_[test_data]
y_test = np.c_[test_labels]
#plt.scatter(x, y , color = 'red')


# For multiclass classification, we will use 'Hobby' as the target
#train_labels_mc = train['Password_i+1_']
#test_labels_mc = test['Password_i+1_']

# Standardize/scale data so it has mean = 0 and variance = 1
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(train_data)
#print(scaler.mean_)
train_data_tr = scaler.transform(train_data)
#scaler.fit(test_data) # Don't! You want to standardize using the training data only
test_data_tr = scaler.transform(test_data)
'''
#print(x.shape[0])
# We use Stochastic Gradient Descent (we will see this later) for classification
#x = x.reshape(-1, x.shape[0])

#The answer of naive bay is too naive.
'''
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x, y)
pswd_predictions = gnb.predict(x_test)
print('Predictions(GaussianNB):', pswd_predictions)

print('\nConfusion matrix: [[TN, FP],[FN,TP]]', confusion_matrix(y_test, pswd_predictions))
'''

from sklearn.svm import SVC
svm_clf = SVC(kernel = 'poly',degree = 4)
svm_clf.fit(x, y)
pswd_predictions = svm_clf.predict(x_test)
# Compare these predictions against the actual values (test_labels)
print('Predictions(SVC):', pswd_predictions) 
print('\nConfusion matrix: [[TN, FP],[FN,TP]]', confusion_matrix(y_test, pswd_predictions))


from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 3)
neigh.fit(x, y)
pswd_predictions = neigh.predict(x_test)
print('Predictions(neigh):', pswd_predictions) 

i = 0
count_match = 0
while (i < 167543):
    if pswd_predictions[i] == y_test[i]:
        count_match = count_match + 1
    i = i + 1
    
ratio = count_match/167543
print(ratio)
    
print('\nConfusion matrix: [[TN, FP],[FN,TP]]', confusion_matrix(y_test, pswd_predictions))



print('Actual     : [', end='')
for i in test_labels:
    print(i, end=' ')

# Now print a confusion matrix
from sklearn.metrics import confusion_matrix
print('\nConfusion matrix: [[TN, FP],[FN,TP]]', confusion_matrix(test_labels, sal_predictions))

# Now use cross-validation and print the scores for each fold
from sklearn.model_selection import cross_val_score
scores = cross_val_score(sgd_clf, train_data_tr, train_labels, cv=3, scoring="accuracy")
print('Score for each fold:', scores)

# Now print a confusion matrix
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, train_data_tr, train_labels, cv=3)
#from sklearn.metrics import confusion_matrix
print('Confusion matrix: [[TN, FP],[FN,TP]', confusion_matrix(train_labels, y_train_pred))

# Obtain Precision and Recall
from sklearn.metrics import precision_score, recall_score
print('Precision:', precision_score(train_labels, y_train_pred))
print('Recall:', recall_score(train_labels, y_train_pred))

# Compute F1 Score
from sklearn.metrics import f1_score
print('F1 Score:', f1_score(train_labels, y_train_pred))

# Multiclass classification 
import numpy as np
sgd_clf.fit(train_data_tr, train_labels_mc) # One vs All (OvA) used by default
some_person = np.random.randint(0, 39) 
print('Predicted:',sgd_clf.predict(train_data_tr[some_person,0:].reshape(1,-1)))
print('Actual:',train.iloc[some_person]['Hobby'])
some_person_scores = sgd_clf.decision_function((train_data_tr[some_person,0:].reshape(1,-1)))

print('Score per class:', some_person_scores)
print('Classes:', sgd_clf.classes_)


y_scores = cross_val_predict(sgd_clf, train_data_tr, train_labels, cv=3, method="decision_function")

from sklearn.metrics import precision_recall_curve
precisions, recalls, thresholds = precision_recall_curve(train_labels, y_scores)
plt.plot(thresholds, precisions[:-1], "b--", label="Precision", linewidth=2)
plt.plot(thresholds, recalls[:-1], "g-", label="Recall", linewidth=2)
plt.xlabel("Threshold", fontsize=16)
plt.legend(loc="upper left", fontsize=16)
plt.ylim([0, 1])
plt.figure(figsize=(8, 6))
#plt.xlim([-700000, 700000])

plt.plot(recalls, precisions, "b-", linewidth=2)
plt.xlabel("Recall", fontsize=16)
plt.ylabel("Precision", fontsize=16)
plt.axis([0, 1, 0, 1])
plt.figure(figsize=(8, 6))

from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(train_labels, y_scores)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, 'g-', linewidth=2, label='SGD')
plt.plot([0, 1], [0, 1], 'k--')
plt.axis([0, 1, 0, 1])
plt.xlabel('False Positive Rate', fontsize=16)
plt.ylabel('True Positive Rate', fontsize=16)

from sklearn.ensemble import RandomForestClassifier
forest_clf = RandomForestClassifier(random_state=42)
y_scoresprobas_forest = cross_val_predict(forest_clf, train_data_tr, train_labels, cv=3, method="predict_proba")
y_scores_forest = y_probas_forest[:, 1] # score = proba of positive class
fpr_forest, tpr_forest, thresholds_forest = roc_curve(train_labels, y_scores_forest)
plt.plot(fpr_forest, tpr_forest, "b:", linewidth=2, label="Random forest")
plt.legend(loc="lower right", fontsize=16)
plt.show()
