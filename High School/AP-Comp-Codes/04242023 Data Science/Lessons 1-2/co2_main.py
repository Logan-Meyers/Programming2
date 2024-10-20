import matplotlib.pyplot as plt
import pandas as pd
import math


# load data from csv
co2_data = pd.read_csv("co2_data.csv", header=5)

# clean bad data
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
co2_data.dropna(subset=['Average'], inplace=True)

# plot data
plt.plot(co2_data["decimal_year"], co2_data["Average"], color='red')
plt.ylabel("Average CO2 PPM")
plt.xlabel("Years")
plt.title("Change in co2")
plt.show()
