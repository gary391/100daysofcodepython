# Open weather_data.csv and use readlines() to create
# a list named data the contains the values from the .csv file.
from pprint import pprint

# def get_data_from_csv(filepath):
#     with open(filepath, mode='r') as file:
#         text = file.readlines()
#     return text
#
# # print(get_data_from_csv('weather_data.csv'))
#
# import csv
#
# def get_data_from_csv_using_csv(filepath):
#     with open(filepath, mode='r') as file:
#         data = csv.reader(file)# this returns a csv object.
#         # each row in the csv file as a separate
#         # list of comma separated element
#         # print(type(data))
#         temperatures = []
#         for row in data:
#             if row[1] != 'temp':
#                 temperatures.append(int(row[1]))
#         # return[int(item) for item in temperatures[1:]]
#         return temperatures
#
# print(get_data_from_csv_using_csv('weather_data.csv'))


import pandas

# data_dict = data.to_dict()
# pprint(data_dict)

# print(type(data['temp']))
# pprint(dir(data["temp"].to_list()))
# total = sum((data["temp"].to_list()))
# avg = total // len(data["temp"].to_list())
# print(avg)

# print(data['temp'].mean())
# print(data['temp'].max())

# Get Data in Columns

# print(data["condition"]) # like dictionary

# Other options
# Your attribute should match the name of the column.
# \If the column starts with a capital letter the
# Attribute will also be capital.
# print(data.condition) # like object

# Get Data in rows
'''
1. Select the column first.
2. Once the column is selected than select the row.

'''

# print(data[data.day == "Monday"])

# high_temp = data['temp'].max()
# print(data[data.temp == high_temp])

# monday = data[data.day == "Monday"]
# # Here the index is important to select the correct value.
# print(monday.temp[0])
# print((monday.temp[0] * 9/5) + 32)


# Create a dataframe from scratch.

# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "count": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data.to_csv('out_color.csv'))


# Create a data frame for squirrels
# data_dict = {
#
# }

gray = 0
red = 0
black = 0
data = pandas.read_csv("2018_CPSCP_Data.csv")
# print(data["Primary Fur Color"])
# for item in (data["Primary Fur Color"]):
#     if item == "Gray":
#         gray = gray + 1
#     elif item == "Cinnamon":
#         red = red + 1
#     elif item == "Black":
#         black = black + 1

data = pandas.read_csv("2018_CPSCP_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"] == "Gray"]) # This will give you the row count that has the squirrel with color gray
red_squirrels_count=len(data[data["Primary Fur Color"] == "Cinnamon"]) # This will give you the row count that has the squirrel with color red
black_squirrels_count=len(data[data["Primary Fur Color"] == "Black"]) # This will give you the row count that has the squirrel with color black.

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
print(data.to_csv('out_color.csv'))

'''
fur, color, count
0, gray, <>
1, red, <>
2, black, <>
'''
df = pandas.read_csv("out_color.csv")
l = df.values.tolist()
print(l) # This will return list of list

# For getting only list you can use flatten
flatten_list = df.values.flatten().tolist()
print(flatten_list)
