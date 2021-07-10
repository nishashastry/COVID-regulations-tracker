import pandas as pd
import numpy as np
import csv
import ssl
from urllib.request import urlopen
import json
ssl._create_default_https_context = ssl._create_unverified_context

import plotly.figure_factory as ff

df_sample = pd.read_csv('http://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'California']

url = 'http://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/latimes-county-totals.csv'
countyCases = pd.read_csv(url, nrows=812, usecols=[2,5], error_bad_lines=False)

countyCasesArray = [[row[col] for col in countyCases.columns] for row in countyCases.to_dict('records')]
values=[]
for c in range(58):
    countyTotal = 0
    for i in range(14):
        countyTotal += countyCasesArray[(i*58)+c][1]
    values.append(countyTotal)

fips = [6001, 6003, 6005, 6007, 6009, 6011, 6013, 6015, 6017, 6019, 6021, 6023, 6025, 6027, 6029, 6031, 6033, 6035, 6037, 6039, 6041, 6043, 6045, 6047, 6049, 6051, 6053, 6055, 6057, 6059, 6061, 6063, 6065, 6067, 6069, 6071, 6073, 6075, 6077, 6079, 6081, 6083, 6085, 6087, 6089, 6091, 6093, 6095, 6097, 6099, 6101, 6103, 6105, 6107, 6109, 6111, 6113, 6115]


colorscale = [
    'rgb(241, 236, 236)',
    'rgb(230, 209, 203)',
    'rgb(221, 182, 170)',
    'rgb(213, 156, 137)',
    'rgb(196, 102, 73)',
    'rgb(186, 74, 47)',
    'rgb(172, 44, 36)',
    'rgb(149, 19, 39)',
    'rgb(120, 14, 40)',
    'rgb(89, 13, 31)'
]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    binning_endpoints=[30, 100, 250, 500, 1000, 2000, 5000, 10000, 20000], colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Covid Cases by County', title='California Counties Covid Cases In The Last 14 Days'
)
fig.layout.template = None
fig.show()


