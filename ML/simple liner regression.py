import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("salary.csv")
x = data.iloc[:,0].values
y = data.iloc[:,1].values

x  = x.reshape(-1,1)
y  = y.reshape(-1,1)
train_x , test_x  , train_y , test_y = train_test_split(x,y,test_size=0.3,random_state=0)
line = LinearRegression()
line.fit(train_x,train_y)
pedic_y = line.predict(test_x)
print(pedic_y)
print(line.intercept_)
plt.scatter(train_x,train_y,color="green")
plt.plot(train_x,line.predict(train_x),color="green")
plt.title('train')
plt.xlabel('exp')
plt.ylabel('salary')
plt.show()
