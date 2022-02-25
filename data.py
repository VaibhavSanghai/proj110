import random
import statistics
import plotly.figure_factory as f
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

fig = f.create_distplot([data], ["reading_time"], show_hist=False)

def randomSetofMean(counter):
    dataF = []
    
    for i in range(0, counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataF.append(value)

    mean2 = statistics.mean(dataF)
    std2 = statistics.stdev(dataF)
    return mean2

def showFig(meanlist):
    dg = meanlist
    dj = f.create_distplot([dg], ["reading_time"], show_hist=False)
    mean = statistics.mean(meanlist)
    std = statistics.stdev(dg)
    print(std)
    dj.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
    dj.show()
    print(mean)

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmean = randomSetofMean(30)
        meanlist.append(setofmean)
    showFig(meanlist)

setup()
