# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go
import math
boundaries = 50

sourceCharges = [[0,1,-1],[5,5,1],[0,2,2]]

masterlist = []
for j in range(boundaries):
    zlist = []
    for i in range(boundaries):
        total = 0
        for charge in sourceCharges:
            distance = math.sqrt(math.pow(i-charge[0],2.0)+math.pow(j-charge[1],2.0))
            
            if distance != 0:
                total +=charge[2] / distance
            else:
                total += charge[2]/0.5
        
        zlist.append(total)
    masterlist.append(zlist)

## y value is index of z
## x value is index of inner list
## z value is number at that point
## indexing list z [y][x]
data = [
    go.Surface(
        z = masterlist)
    ]

layout = go.Layout(
    title='Electric Potential',
    autosize=True,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Electric Potential')
