# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# #
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average_temp = data["temp"].mean()
max_temp = data["temp"].max()
#
# print(temp_list)
#
# print(average_temp)
#
# print(max_temp)

#Get Data in Row

print(data[data.day == "Monday"])

print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]

print(monday.temp)

# celsius = monday.temp
#
# celsius_type = celsius.astype(int)
#
celsiusa = (monday.temp * 9/5) + 32

print(float(celsiusa))