from email.policy import default
import streamlit as st
import pickle



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