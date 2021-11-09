import statistics
import plotly.figure_factory as ff
import random
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("temp-data.csv")
data = df["temp"].to_list()

def random_set_of_mean(counter):

    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist= False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean : ",mean)

setup()

def stdev():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    stdev = statistics.stdev(mean_list)
    print("Standard Deviation : ",stdev)

stdev()
