# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = pd.read_csv("temperature_data.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
plt.plot(temp_data["Year"], temp_data["Anomaly"], color='red')
plt.ylabel("Temperature Anomalies in Celsius")
plt.xlabel("Years")
plt.title("Change in Temperatures")

# TODO #3: Plot LOWESS in a line graph
plt.plot(temp_data["Year"], temp_data["LOWESS"], color='blue')

# TODO #4: Use matplotlib to make a bar chart
# plt.bar(temp_data["Year"], temp_data["Anomaly"], color='red')
# plt.bar(temp_data["Year"], temp_data["LOWESS"], color='blue')

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = temp_data["Anomaly"][0]
max_anomaly = temp_data["Anomaly"][0]
min_year = temp_data["Year"][0]
max_year = temp_data["Year"][0]
sum_anomaly = 0
avg_anomaly = 0

# find the min, max, and calculate the sum
for i in range(len(temp_data["Anomaly"])):
    if (temp_data["Anomaly"][i] < min_anomaly):
        min_anomaly = temp_data["Anomaly"][i]
        min_year = temp_data["Year"][i]
    
    if (temp_data["Anomaly"][i] > max_anomaly):
        max_anomaly = temp_data["Anomaly"][i]
        max_year = temp_data["Year"][i]

    sum_anomaly += temp_data["Anomaly"][i]

# average sum divide by amount of years (largest - smallest)
avg_anomaly = sum_anomaly / len(temp_data["Anomaly"])

print(f"MIN:   amount: {min_anomaly}; year: {min_year}")
print(f"MAX:   amount: {max_anomaly}; year: {max_year}")
print(f"OTHER: sum: {sum_anomaly}; average: {avg_anomaly}")

# show graph
plt.show()
