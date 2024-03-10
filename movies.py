import streamlit as st
import pandas as pd
import numpy as np

# In order to quit out of the running server in the CMD window, hit CTRL + C 


st.write("""
         This is an app for some Movie titles!
         """
        )

st.sidebar.header("User data")
st.sidebar.markdown("""
                    [CSV input file]
                    """)

file = st.sidebar.file_uploader('Upload csv', type=['csv'])

if file is not None:
    df = pd.read_csv(file)

st.sidebar.selectbox('Test1', ('one', 'two', 'three'))
st.sidebar.slider('Some tag', 30, 60, 40)
st.sidebar.text_input('Name: ')

