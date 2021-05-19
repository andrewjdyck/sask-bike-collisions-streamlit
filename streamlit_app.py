import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# get data
@st.cache
def get_data():
    return(pd.read_csv('https://raw.githubusercontent.com/andrewjdyck/sask-bike-collisions/master/data/regina.csv'))

@st.cache
def get_map_data():
    return(get_data()[["lat", "lon"]].dropna())

map_df = get_map_data()


# Start the UI

st.header('Bicycle collisions in Regina, SK')
st.subheader('Visualizing bicycle collision risk with AI')


splash_map = st.beta_container()

st.subheader('Here is some analysis.')
eda_summary = st.beta_container()


eda_summary.write(get_data().head())

splash_map.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=50.45,
        longitude=-104.62,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
        'HexagonLayer',
        data=map_df,
        get_position='[lon, lat]',
        radius=200,
        elevation_scale=4,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=map_df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))




