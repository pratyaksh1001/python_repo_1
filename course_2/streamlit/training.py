from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

df=pd.read_csv("obesity_data.csv")
df.replace({"Male":1,"Female":0},inplace=True)
x=df.drop("ObesityCategory",axis=1)
y=pd.get_dummies(df["ObesityCategory"]).replace({True:1,False:0})
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=RandomForestClassifier()
model.fit(x_train,y_train)
print(df["ObesityCategory"].unique())
#pickle.dump(model,open("model.pkl","wb"))