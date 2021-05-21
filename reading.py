import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

def random_set_mean(c):
    dataset=[]
    for i in range(0,c):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
   df=mean_list
   mean=statistics.mean(df)
   fig=ff.create_distplot([df],["reading_time"],show_hist=False)
   fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
   fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_off_mean=random_set_mean(30)
        mean_list.append(set_off_mean)
    show_fig(mean_list)

setup()

mean=statistics.mean(data)
print("Mean of Sampling Destribution is:",mean)