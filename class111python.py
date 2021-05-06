import pandas as pd
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("class111data.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math Scores"], show_hist = False)
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean of population data is: ", mean)
print("STDEV of population data is: ", stdev)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    setOfMeans = random_set_of_means(100)
    mean_list.append(setOfMeans)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of sample data is: ", mean)
print("STDEV of sample data is: ", std_deviation)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.4], mode = "lines", name = "Mean"))
#fig.show()

first_stdev_start = mean-std_deviation
first_stdev_end = mean+std_deviation

second_stdev_start = mean-(std_deviation*2)
second_stdev_end = mean+(std_deviation*2)

third_stdev_start = mean-(std_deviation*3)
third_stdev_end = mean+(std_deviation*3)

print("Std 1: ", first_stdev_start, first_stdev_end)
print("Std 2: ", second_stdev_start, second_stdev_end)
print("Std 3: ", third_stdev_start, third_stdev_end)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.4], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #1 Start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #1 End"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #2 Start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #2 End"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #3 Start"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #3 End"))
#fig.show()

df = pd.read_csv("int1.csv")
data = df["Math_score"].tolist()
mean_of_sample_1 = statistics.mean(data)
print("Samle 1 mean:", mean_of_sample_1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.4], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y = [0, 0.4], mode = "lines", name = "Mean of Sample #1"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #1 Start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #1 End"))
#fig.show()

df = pd.read_csv("int2.csv")
data = df["Math_score"].tolist()
mean_of_sample_2 = statistics.mean(data)
print("Samle 2 mean:", mean_of_sample_2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.4], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_2, mean_of_sample_2], y = [0, 0.4], mode = "lines", name = "Mean of Sample #2"))
# fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #1 Start"))
# fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #1 End"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #2 Start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #2 End"))
fig.show()

df = pd.read_csv("int3.csv")
data = df["Math_score"].tolist()
mean_of_sample_3 = statistics.mean(data)
print("Samle 3 mean:", mean_of_sample_3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.4], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_3, mean_of_sample_3], y = [0, 0.4], mode = "lines", name = "Mean of Sample #3"))
# fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #1 Start"))
# fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #1 End"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #2 Start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #2 End"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.5], mode = "lines", name = "STDEV #3 Start"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.5], mode = "lines", name = "STDEV #3 End"))
fig.show()