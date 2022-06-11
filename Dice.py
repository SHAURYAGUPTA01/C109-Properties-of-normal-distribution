import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result =[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

mean = statistics.mean(dice_result)
std = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

# print("Mean of data is  : {}".format(mean))
# print("Median of data is : {} ".format(median))
# print("Mode of data is : {} ".format(mode))



first_std_start , first_std_end = mean-std , mean+std

second_std_start , second_std_end = mean - (2*std) , mean + (2*std)

third_std_start , third_std_end = mean - (3*std) , mean + (3*std)

fig = ff.create_distplot( [dice_result] , ["result"] , show_hist = False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines+markers", name="MEAN of data" ))

fig.add_trace(go.Scatter(x = [first_std_start,first_std_start] , y = [0 , 0.17] , mode = "lines", name = "First STD Start"))

fig.add_trace(go.Scatter(x = [first_std_end,first_std_end] , y = [0 , 0.17] , mode = "lines", name = "First STD end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start] , y = [0 , 0.17] , mode = "lines", name = "Second STD Start"))

fig.add_trace(go.Scatter(x = [second_std_end,second_std_end] , y = [0 , 0.17] , mode = "lines", name = "Second STD end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start] , y = [0 , 0.17] , mode = "lines", name = "Third STD Start"))

fig.add_trace(go.Scatter(x = [third_std_end,third_std_end] , y = [0 , 0.17] , mode = "lines", name = "Third STD end"))

fig.show()

data_within_std1 = [i for result in dice_result if result > first_std_start and result < first_std_end]

data_within_std2 = [i for result in dice_result if result > second_std_start and result < second_std_end]

data_within_std3 = [i for result in dice_result if result > third_std_start and result < third_std_end]
print("\n")
print("{} % of data lies within 1st standard deviation".format(len(data_within_std1) * 100 / len(dice_result)))
print("{} % of data lies within 2nd standard deviation".format(len(data_within_std2) * 100 / len(dice_result)))
print("{} % of data lies within 3rd standard deviation".format(len(data_within_std3) * 100 / len(dice_result)))