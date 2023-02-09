import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

data=pd.read_csv("Tennisdata.csv")
print("The 5 values of data is :\n",data.haed())

x=data.iloc[:,:-1]
print("The 5 values of table data is\n",x.head())

y=data.iloc[:,-1]
print("The 5 values of table data output is\n",y.head())

le_outlook=LabelEncoder()
x.outlook=le_outlook.fit_transform(x.outlook)

le_temp=LabelEncoder()
x.temp=le_temp.fit_transform(x.temp)

le_humidity=LabelEncoder()
x.humidity=le_humidity.fit_transform(x.humidity)

le_playtennis=LabelEncoder()
y.playtennis=le_playtennis.fit_transform(y.playtennis)

print("The final output of data\n",data.haed())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

classifier=GaussianNB()
classifier.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
print("Accuracy is:",classifier.fit(accuracy_score(x_test),y_test))