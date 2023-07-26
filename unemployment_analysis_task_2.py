# -*- coding: utf-8 -*-
"""unemployment_analysis_task-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15A9L5v-suLtjIBbX-hWjlbr7Nr35MdlU
"""

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df=pd.read_csv("Unemployment in India.csv")

df.head()

df.tail()

df.info()

df.shape

df.describe()

x=df['Region']
x

y=df[' Estimated Unemployment Rate (%)']
y

df2=df.iloc[:,3]
df2

fg=px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemployment Rate (Region-Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Scatter Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()