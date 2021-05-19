import streamlit as st
import pandas as pd

# get data
@st.cache
def get_data():
    return(pd.read_csv('https://raw.githubusercontent.com/andrewjdyck/sask-bike-collisions/master/data/regina.csv').head())

# Start the UI

st.header('Bicycle collisions in Regina, SK')
st.subheader('Visualizing bicycle collision risk with AI')

splash_map = st.beta_container()

splash_map.write(get_data())


