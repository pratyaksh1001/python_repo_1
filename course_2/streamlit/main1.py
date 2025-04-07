import streamlit as st
import pandas as pd
import  numpy as np


st.title("hello world")
st.write("simple text")

df=pd.DataFrame({
    "col1":[1,2,3,4,5],
    "col2":[2,3,4,5,6],
    "col3":[3,4,5,6,7]
})
df.to_csv("data.csv")
st.write(df)

st.line_chart(df)

char_data=pd.DataFrame(np.random.randn(20,5),columns=['col1','col2','col3',"col4","col5"])
st.line_chart(char_data)