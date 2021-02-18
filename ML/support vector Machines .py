import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

dataset = pd.read_csv("Social_Network_Ads.csv")
sc = StandardScaler()
X=dataset.iloc[:, [2,3]].values
y=dataset.iloc[:, 4].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.10)
cls_svc = SVC(kernel="linear")
cls_svc.fit(X_train,y_train)
y_prect = cls_svc.predict(X_train)
cm = confusion_matrix(X_test,y_prect)
x_set, y_set = X_train,y_train