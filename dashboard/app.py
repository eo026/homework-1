#-------------------#
# SETUP
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


from pathlib import Path
import datetime as dt
from datetime import datetime


#-------------------#
# IMPORT LOCAL DATA


# Data import (you may need to change the path)
df = pd.read_csv( "https://raw.githubusercontent.com/eo026/homework-1/main/data/external/data.csv")


###-------------------###
# START OF OUR APP

#-------------------#
# HEADER

# Title of our app
st.title("Unsere Visualisierungen")

# Add image
st.image('hdm-logo.jpg')

# Add header
st.header("Dashboard Gruppe E")

#-------------------#
# SIDEBAR

# Header
st.sidebar.header("This is my sidebar")

# Make a slider
satisfaction = st.sidebar.slider('What is your life satisfaction?', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("My life satisfaction is around ", satisfaction, 'points')

#-------------------#
# BODY

st.write("Take a look at my data")
# Show static DataFrame
st.dataframe(df)

st.write("Take a look at my chart")
# Make a chart with altair
#Visualisierung 1
c = alt.Chart(df).mark_circle().encode(
     x='Gender', 
     y='Race 1', 
     color='Gender'
     )

chartRace = alt.Chart(df).mark_arc().encode(
    theta=alt.Theta(field="index", type="quantitative"),
    color= alt.Color ('Gender', 
                     legend=alt.Legend(title="Gender")),
    tooltip = ["Gender"]
).properties( 
    title= 'Which gender are the candidates?',
    width= 300,
    height= 300

).configure_title(
    fontSize=15,
    font='Arial',
    anchor='start',
    color='black'
)

pie = chartRace.mark_arc(outerRadius=70)

pie


# Bar chart
st.subheader("Bar chart")

c = alt.Chart(df).mark_bar().encode(
    x='Gender',
    y='Race 1',
    tooltip = ['Gender', "Race 1"]
)

st.altair_chart(c, use_container_width=True)

# Show metric
st.subheader("Display Metrics")
st.metric("My metrics", 32, 4)

# Add slider with user input
st.subheader("Slider")
st.write("This is a Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Show metric
st.subheader("Display Metrics")
st.metric("My metrics", 32, 4)

# Add slider with user input
st.subheader("Slider")
st.write("This is a Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

###-------------------###
# END OF APP