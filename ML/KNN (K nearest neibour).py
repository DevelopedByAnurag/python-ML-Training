import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
dataset = pd.read_csv("Social_Network_Ads.csv")
X=dataset.iloc[:, [2,3]].values
y=dataset.iloc[:, 4].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.10)
# StandardScaler normalizes the data which helps to increase accuracy and reducing errors
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
# minkowski we are calculting distance formula.
classifer = KNeighborsClassifier(n_neighbors=9,metric='minkowski',p=2)
classifer.fit(X_train,y_train)
y_predict =  classifer.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict)
print(cm)
x_set,y_set =X_test,y_test
# .arrange runs a function like loop from start to end range
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:, 0].max()+1,step=0.01),np.arange(start=x_set[:, 1].min()-1,stop=x_set[:, 1].max()+1,step=0.01))
# .T means tranpose
# alpha means trasparancy
# ListedColormap create a color map as in img knn.png seprating two colors
plt.contourf(x1,x2,classifer.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x1.min(),x1.max())
# Enumrate x contains counter(index) and j cotains the actual loop
for x,j in enumerate(np.unique(y_set)):
	plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(("red","green"))(x),label=j)
plt.title("knn")
plt.xlabel("age")
plt.ylabel("estimated Sallary")
# legend displays the counter as in the top of knn.png
plt.legend()
plt.show()