from email.policy import default
import streamlit as st
import pickle
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


ref=['Normal weight', 'Obese', 'Overweight', 'Underweight']
gender_ref={"Male":1,"Female":0}
age=st.slider("enter age",10,110,20)
gender=gender_ref[st.selectbox("select gender",["Male","Female"])]
height=st.slider("select height in cm",50,250,150)
weight=st.slider("select weight in kg",10,200,40)
bmi=weight/(height*height)
physical_activity=st.selectbox("select physical activity",["not at all","sometimes","frequently","very regularly"])
ref_2={"not at all":1,"sometimes":2,"frequently":3,"very regularly":4}
physical_activity=ref_2[physical_activity]
l=[age,gender,height,weight,bmi,physical_activity]
with open("model.pkl","rb") as f:
    model=pickle.load(f)
print(model.predict([l,])[0].argmax())
if l:
    st.title(f"you are {ref[model.predict([l,])[0].argmax()]}")