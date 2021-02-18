import sklearn
from sklearn import svm
#from sklearn import train_test_split
from sklearn import datasets
#import dataset
cancer = datasets.load_breast_cancer()
#prints the name of  rows
print(cancer.feature_names)
x = cancer.data 
y = cancer.target

#x_train , x_test ,y_train , y_test =  train_test_split(x,y,test_size=)


#clf = svm.svc()
#clf.fit(x_train,y_train)