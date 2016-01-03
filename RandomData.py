# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go
import math

sourceCharges = []
cont = "y"
import pickle
#if input("Use Previous Source Charges (y/n)? ") != "n":
try:
    file = open("RandomFile","rb")
    sourceCharges = pickle.load(file)
    file.close()
    print ("File Found")
    #cont = input("Do you want to enter more source charges (y/n)? ")

except:
    print ("File not Found.  Creating a new one.")
    file = open("RandomFile", "wb")
    file.close()
boundaries = 10
for num in range(0,10):
    import random
    xcord = random.randrange(0,10)
    ycord = random.randrange(0,10)
    charge = random.randrange(-5,6)
    sourceCharges.append([xcord,ycord,charge])
print (sourceCharges)
##while cont != "n":
##    xcord = int(input("Enter the X Cordinate: "))
##    ycord = int(input("Enter the Y Cordinate: "))
##    charge = int(input("Enter the charge: "))
##    sourceCharges.append([xcord,ycord,charge])
##    cont = input("Do you want to enter more source charges (y/n)? ")
file = open("RandomFile", "wb")
pickle.dump(sourceCharges, file)
file.close()
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
                total += charge[2]/0.8
        
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
