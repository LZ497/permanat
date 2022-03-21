# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import altair as alt
import streamlit as st
import time

family_4 = pd.read_csv('family_4.csv')
family_5 = pd.read_csv('family_5.csv')
family_6 = pd.read_csv('family_6.csv')

family_4['date'] = pd.to_datetime(family_4['date'])
family_5['date'] = pd.to_datetime(family_5['date'])
family_6['date'] = pd.to_datetime(family_6['date'])

df=family_4

lines = alt.Chart(df).mark_line().encode(
     x=alt.X('1:T',axis=alt.Axis(title='date')),
     y=alt.Y('0:Q',axis=alt.Axis(title='value'))
).configure_axis(
    labelFontSize=32,
    titleFontSize=32
).properties(
    width=800,
    height=600
)
  

def plot_animation(df):
    lines = alt.Chart(df).mark_line().encode(
       x=alt.X('date:T', axis=alt.Axis(title='date')),
       y=alt.Y('worktime:Q',axis=alt.Axis(title='worktime')),
       color='plug'
).configure_axis(
    labelFontSize=24,
    titleFontSize=24
).properties(
        title="Different plugs worktime",
        width=800,
        height=600
).configure_title(fontSize=24
).configure_legend(titleFontSize=24,labelFontSize=24)
                  
    return lines    


N = df.shape[0] # number of elements in the dataframe
burst =36      # number of elements (months) to add to the plot
size = burst 
line_plot = st.altair_chart(lines)
start_btn = st.button('Start')
if start_btn:
   for i in range(1,N):
      step_df = df.iloc[0:size]
      lines = plot_animation(step_df)
      line_plot = line_plot.altair_chart(lines)
      size = i + burst
      if size >= N: 
         size = N - 1
      time.sleep(0.001)
