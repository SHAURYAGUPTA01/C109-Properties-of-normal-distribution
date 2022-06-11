import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("height-weight.csv")
hlist = df["Height(Inches)"].tolist()

mean = statistics.mean(hlist)
std = statistics.stdev(hlist)
median = statistics.median(hlist)
mode = statistics.mode(hlist)

print("Mean of data is  : {}".format(mean)) 
print("Median of data is : {} ".format(median))
print("Mode of data is : {} ".format(mode))

first_std_start , first_std_end = mean-std , mean+std

second_std_start , second_std_end = mean - (2*std) , mean + (2*std)

third_std_start , third_std_end = mean - (3*std) , mean + (3*std)

fig = ff.create_distplot( [hlist] , ["result"] , show_hist = False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines+markers", name="MEAN of data" ))

fig.add_trace(go.Scatter(x = [first_std_start,first_std_start] , y = [0 , 0.17] , mode = "lines", name = "First STD Start"))

fig.add_trace(go.Scatter(x = [first_std_end,first_std_end] , y = [0 , 0.17] , mode = "lines", name = "First STD end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start] , y = [0 , 0.17] , mode = "lines", name = "Second STD Start"))

fig.add_trace(go.Scatter(x = [second_std_end,second_std_end] , y = [0 , 0.17] , mode = "lines", name = "Second STD end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start] , y = [0 , 0.17] , mode = "lines", name = "Third STD Start"))

fig.add_trace(go.Scatter(x = [third_std_end,third_std_end] , y = [0 , 0.17] , mode = "lines", name = "Third STD end"))

fig.show()

data_within_std1 = [result for result in hlist if result > first_std_start and result < first_std_end]

data_within_std2 = [result for result in hlist if result > second_std_start and result < second_std_end]

data_within_std3 = [result for result in hlist if result > third_std_start and result < third_std_end]
print("\n")
print("{} % of data lies within 1st standard deviation".format(len(data_within_std1) * 100 / len(hlist)))
print("{} % of data lies within 2nd standard deviation".format(len(data_within_std2) * 100 / len(hlist)))
print("{} % of data lies within 3rd standard deviation".format(len(data_within_std3) * 100 / len(hlist)))