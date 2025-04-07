import streamlit as st
import pandas as pd
import numpy as np


st.title("streamlit app")

name=st.text_input("enter the name")
age=st.slider("enter the age",10,50,25)
if age>20:
    st.write("valid")
else:
    st.write("invalid")
options=["Python","C++","Java","Rust","Go","Swift"]

if name:
    st.write(f"hello {name}")
language=st.selectbox("select",options)

file=st.file_uploader("upload CSV")
if file:
    df=pd.read_csv(file)
    st.write(df)