import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing  import StandardScaler
from sklearn.linear_model import LogisticRegression
#%matplotlib inline
data = pd.read_csv('Social_Network_Ads.csv')
real_x = data.iloc[:,2:3].values
real_y = data.iloc[:,4].values
sc = StandardScaler()

x_train = sc.fit_transform(x_train)

classifier = LogisticRegression
classifier.fit(x_train,y_train)

y_predict = classifier.predict(x_train)

for x in range(len(y_predict)):
	print("predicted", y_predict[x], "  Actual : ", y_test[x])




X_set,y_set=X_train,y_train
#helps in distributing data
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:, 0].max()+1,step=0.01)
                  ,np.arange(start=X_set[:, 1].min()-1,stop=X_set[:, 1].max()+1,step=0.01))
#divides logistic regression graph
plt.contourf(X1,X2,classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
plt.title('Logistic regression(Training set)')
plt.xlabel('age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()











plt.scatter(real_x,real_y,color="red")
plt.plot(x_grid,reg.predict(x_grid),color="blue")
plt.title("DecisionTree model")
plt.xlabel("Position level")
plt.ylabel("sallary")
plt.show()
