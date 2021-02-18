import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt 
#%matplotlib inline

data = pd.read_csv('Position_Salaries.csv')

real_x = data.iloc[:,1:2].values
real_y = data.iloc[:,2].values

reg = RandomForestRegressor(n_estimators=10)
reg.fit(real_x,real_y)

y_predict = reg.predict(real_x)

x_grid = np.arange(min(real_x),max(real_y),0.01)
x_grid = x_grid.reshape((len(x_grid),1))



plt.scatter(real_x,real_y,color="red")
plt.plot(x_grid,reg.predict(x_grid),color="blue")
plt.title("DecisionTree model")
plt.xlabel("Position level")
plt.ylabel("sallary")
plt.show()
