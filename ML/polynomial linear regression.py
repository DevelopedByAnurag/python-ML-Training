import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt 

data = pd.read_csv('Position_Salaries.csv')

real_x = data.iloc[:,1:2].values
real_y = data.iloc[:,2].values

linear_reg = LinearRegression()
linear_reg.fit(real_x,real_y)
print(linear_reg.predict([[6.5]]))


poly_regression = PolynomialFeatures(degree=15)
real_x_poly = poly_regression.fit_transform(real_x)


poly_regression.fit(real_x_poly,real_y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

linear_reg2=LinearRegression()
linear_reg2.fit(real_x_poly,real_y)



plt.scatter(real_x,real_y,color="red")
plt.plot(real_x,linear_reg.predict(real_x),color="blue")
plt.title("linear model")
plt.xlabel("Position level")
plt.ylabel("sallary")
plt.show()


plt.scatter(real_x,real_y,color="red")
plt.plot(real_x,linear_reg2.predict(real_x_poly),color="blue")
plt.title("Polinomial linear model")
plt.xlabel("Position level")
plt.ylabel("sallary")
plt.show()