# with open ("weather_data.csv", 'r') as file:
#    data = (file.readlines())
#    print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
# print(temperature)

# print(type(data)) # data frame is equivalent to a sheet in excel
# print(type(data['temp'])) # series is equivalent to a list or a column
# print(data['temp']) # you can get column data with a specific header
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].tolist()
# print(temp_list)
#
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data['temp'].max())
# print(data['condition'])# using it as a dictionary
# print (data.condition) # using as a object

# Get data in row
# print(data[data.day == 'Monday'])

# Find the row that has the highest temperature of the week
# print(data['temp'].max())
# print(data[data.temp == data.temp.max()])

monday_temp = data[data.day == 'Monday']
# monday_temp = data[data['day'] == 'Monday']
# print(monday_temp.temp)
print(monday_temp.temp[0])  #This will give the zero value of the temp.
# monday_temp_f = int(monday_temp.temp[0]) * 9/5 + 32
# print(monday_temp_f)
#
# # Create a data frame from stratch
#
# data_dict = {
#     "students" : ['Amy', 'John', 'Mike'],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data.to_csv("new_data.csv"))

import pandas
data = pandas.read_csv("2018_CPS_Data.csv")
'''
final csv with columns - fur, color, count
'''
# series is equivalent to a list or a column
g_squirrel = data[data["Primary Fur Color"] == "Gray"]
c_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
b_squirrel = data[data["Primary Fur Color"] == "Black"]

'''
Gray
Cinnamon
Black
'''
print(len(g_squirrel))
print(len(c_squirrel))
print(len(b_squirrel))

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [2473, 392, 103]

}
data = pandas.DataFrame(data_dict)
print(data.to_csv("new_squirrel_data.csv"))

