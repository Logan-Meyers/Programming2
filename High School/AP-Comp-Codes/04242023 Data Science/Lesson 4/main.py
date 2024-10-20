from matplotlib import pyplot as plt
import pandas as pd


# read csv data into a data frame object
honeyDF = pd.read_csv("honey.csv", header=0)

# clean string data
honeyDF['Value'] = honeyDF['Value'].str.replace(",","")  # remove commas
honeyDF['Value'] = pd.to_numeric(honeyDF['Value'], errors='coerce')  # convert numbers to numeric or else NaN
honeyDF.dropna(subset=['Value'], inplace=True)  # drop NaN values in the Value column

# organize data for each state
unique_states = honeyDF['State'].unique()
all_honey = []
all_states = []
for state in unique_states:
    # match state, group by year, get value
    honey_data = honeyDF[honeyDF['State'] == state].groupby('Year')['Value']
    # sum the values and store in an array
    all_honey.append(honey_data.sum())
    # store the state
    all_states.append(state)

for thing in all_honey:
    print("yup")
    print(thing)
    print(type(thing))

# print(all_honey)
for i in range(len(all_honey)):
    # get the state and its honey values
    honey = all_honey[i]
    state = all_states[i]
    # the keys in the honey data structure are the years
    years = honey.keys()
