import pandas as pd 
import numpy as np 
import sklearn 
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
from sklearn.model_selection import train_test_split
#from matplotlib.colors import ListedColormap
dataset = pd.read_csv("car.data")
# converts words in numbers accoringly for eazy catagorizing the values
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(dataset["buying"]))
maint = le.fit_transform(list(dataset["maint"]))
doors = le.fit_transform(list(dataset["doors"]))
persons = le.fit_transform(list(dataset["persons"]))
lug_boot = le.fit_transform(list(dataset["lug_boot"]))
safety = le.fit_transform(list(dataset["safety"]))
clas = le.fit_transform(list(dataset["class"]))
x = list(zip(buying,persons,lug_boot,safety))
y = list(clas)
X_train,X_test,y_train,y_test= train_test_split(x,y,test_size=0.1)
predict = "class"   #optional
model = KNeighborsClassifier(n_neighbors=9)
model.fit(X_train,y_train)
acc = model.score(X_test,y_test)
print(acc)
predicted = model.predict(X_test)
cm = confusion_matrix(y_test,predicted)
print(cm)
names = ["unacc","acc","good","vgood"]
for x in range(len(predicted)):
	print("predicted: " , names[predicted[x]],"data: ", X_test[x],"actual: ", names[y_test[x]])
	n= model.kneighbors([X_test[x]],9,True)
	print("n ",n)

