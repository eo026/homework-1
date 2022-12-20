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

#Visualisierung 1

st.subheader("Pie Chart")

df['Gender'] = df['Gender'].astype("category")
source = df[['Gender']]
source = source.reset_index()

chartRace = alt.Chart(source).mark_arc().encode(
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


# Visualisierung 2
st.subheader("Horizontal Bar Chart")

df['State'] = df['State'].astype("category")

ChartState = alt.Chart(df).mark_bar().encode(
    x=alt.X('count(State)',              
            axis=alt.Axis(title = "Count")),
    y=alt.X('State', 
            axis=alt.Axis(title="State", 
                          labelAngle=0)), 
    color=alt.Color('State', scale=alt.Scale(scheme='set3')),
    tooltip = ["count(State)","State"]

).interactive(    

).properties(title='Count of candidates in the states',
             width=400,
             height=800
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='black'
)
ChartState

# Visualisierung 3
st.subheader("Normalized Stacked Bar Chart")

df['State'] = df['State'].astype("category")
df['Gender'] = df['Gender'].astype("category")

alt.Chart(df).mark_bar().encode(
    x=alt.X('count(Gender)', stack="normalize",
        axis=alt.Axis(title = "Proportion of male and female candidates")),
    y=alt.Y('State',
        axis=alt.Axis(title = "State")),
    color='Gender',
    tooltip=["Gender", "count(Gender)", "State"]
).interactive(
).properties(title='Proportion of male and female candidates in the states',
             width=400,
             height=800
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='black'
)

# Visualisierung 4
st.subheader("Horizontal Stacked Bar Chart")

df['Race 1'] = df['Race 1'].astype("category")
alt.Chart(df).mark_bar().encode(
    x=alt.X('count(Race 1)',
        axis=alt.Axis(title = "Count")),
    y=alt.Y('State',
        axis=alt.Axis(title = "State")),
    color='Race 1',
    tooltip=["Race 1", "count(Race 1)", "State"]
).interactive(
).properties(title='Count of candidates in the states by race',
             width=400,
             height=800
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='black'
)

###-------------------###
# END OF APP