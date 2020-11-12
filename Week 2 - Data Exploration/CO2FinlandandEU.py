import plotly
import plotly.express as ex
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from scipy.io import netcdf
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib
import matplotlib.pyplot as plt
import sklearn
%matplotlib inline

df = pd.read_csv("gases.csv")
df.head()
graph = pd.pivot_table(df, values='value', index=['country_or_area', 'year'], columns=['category'])
graph.head()
finland_df = df[df.country_or_area == 'Finland'][['year','category', 'value']]
eu_df = df[df.country_or_area == 'European Union'][['year', 'category', 'value']]

fig = go.Figure(layout = go.Layout(
        xaxis=dict(showgrid = True,title = "year",color = 'black'),
        yaxis=dict(showgrid = True,title = "value",color = 'black'),
    ))

fig.add_trace(go.Scatter(
                x=finland_df.year,
                y=finland_df['carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent'],
                name="CO2 emissions",
                line_color='rgb(203, 67, 53)',
                opacity=0.8))
fig.update_layout(title_text = "Change in CO2 between 1880 ~ 2016", title_x=0.5, title_font_family="Times New Roman", \
                  title_font_size = 22, paper_bgcolor = 'rgba(233,233,233,1)', plot_bgcolor = 'rgba(240,235,228,1)')
fig.show()
fig = go.Figure(layout = go.Layout(
        xaxis=dict(showgrid = True,title = "year",color = 'black'),
        yaxis=dict(showgrid = True,title = "value",color = 'black'),
    ))

fig.add_trace(go.Scatter(
                x=eu_df.year,
                y=eu_df['carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent'],
                name="CO2 emissions",
                line_color='rgb(203, 67, 53)',
                opacity=0.8))
fig.update_layout(title_text = "Change in CO2 between 1880 ~ 2016", title_x=0.5, title_font_family="Times New Roman", \
                  title_font_size = 22, paper_bgcolor = 'rgba(233,233,233,1)', plot_bgcolor = 'rgba(240,235,228,1)')
fig.show()