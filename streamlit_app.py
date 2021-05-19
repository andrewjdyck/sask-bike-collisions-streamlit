import streamlit as st
import pandas as pd

rd = pd.read_csv('https://raw.githubusercontent.com/andrewjdyck/sask-bike-collisions/master/data/regina.csv')

st.write(rd.head())
