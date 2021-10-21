# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = list()
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data["condition"])

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
