# This is the code for storing the data in a list without using external libraries
# with open("002 weather-data.csv") as weather:
#     weather_data = weather.read().split()
# print(weather_data)


# This is the code for the CSV

# import csv
# with open("002 weather-data.csv") as weather:
#     weather_data = csv.reader(weather)
#     temperatures = []
#     weather_data.__next__()
#     for row in weather_data:
#         temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv('002 weather-data.csv')
temperatures = data['temp'].to_list()

totaltemp = 0
for temp in temperatures:
    totaltemp += temp
print(f"The average temperature is: {totaltemp/len(temperatures):.2f}")
highesttemp = data['temp'].max()

print(f"The highest temperature is {highesttemp}")

print(data[data.temp == highesttemp])