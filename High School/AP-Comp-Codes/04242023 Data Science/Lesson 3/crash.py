import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import calendar


def closest_num(num, num_list):
    """
    Given a number and a list of numbers, returns the number from the list
    that is closest to the given number.
    (Written by ChatGPT)
    """
    closest = None
    diff = float('inf')  # Initialize with a very large number
    
    for n in num_list:
        if abs(num - n) < diff:
            diff = abs(num - n)
            closest = n
    
    return closest

def crashesPerMonth():
    # create dictionary holding months and crashes
    monthDict = {}
    totalCrashes = 0

    # set dictionary to 0 at each month
    for month in calendar.month_name:
        if month != '':
            monthDict[month] = 0
    
    # read entire file and set to dataframe
    entireDF = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes (1).csv", header=0)

    # for each crash, add 1 to the matching month, and to the total
    for date in entireDF["CRASH DATE"]:
        # get just the month
        month = int(date[:2])
        # get month name
        monthName = calendar.month_name[month]
        # incrememnt
        monthDict[monthName] += 1
        totalCrashes += 1

    def getAutopctVal(slicePercent):
        percentToApproxVal = totalCrashes * (slicePercent/100)
        closestVal = closest_num(percentToApproxVal, monthDict.values())
        return closestVal
    
    colors = ["#00dfab", "#00ff0a", "#008b05", "#b02af5", "#c1a8f9", "#f6cd8b", "#ed754a", "#ec6148", "#ff0000", "#0000ff", "#0067ff", "#00b6ff"]
    explode = [0.05 for _ in range(12)]

    plt.pie(list(monthDict.values()), labels=list(monthDict.keys()), autopct=getAutopctVal, counterclock=False, startangle=90, pctdistance=0.825, colors=colors, explode=explode)
    plt.title("Crashes per month")
    plt.show()

def reasonsForCrash():
    # create dictionary holding months and crashes
    crashDict = {}
    totalCrashes = 0

    # set dictionary to 0 at each month
    for month in calendar.month_name:
        if month != '':
            crashDict[month] = 0
    
    # read entire file and set to dataframe
    entireDF = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes (1).csv", header=0)

    # for each crash, add 1 to the matching month, and to the total
    for date in entireDF["CRASH DATE"]:
        # get just the month
        month = int(date[:2])
        # get month name
        monthName = calendar.month_name[month]
        # incrememnt
        crashDict[monthName] += 1
        totalCrashes += 1

    def getAutopctVal(slicePercent):
        percentToApproxVal = totalCrashes * (slicePercent/100)
        closestVal = closest_num(percentToApproxVal, crashDict.values())
        return closestVal
    
    colors = ["#00dfab", "#00ff0a", "#008b05", "#b02af5", "#c1a8f9", "#f6cd8b", "#ed754a", "#ec6148", "#ff0000", "#0000ff", "#0067ff", "#00b6ff"]
    explode = [0.05 for _ in range(12)]

    plt.pie(list(crashDict.values()), labels=list(crashDict.keys()), autopct=getAutopctVal, counterclock=False, startangle=90, pctdistance=0.825, colors=colors, explode=explode)
    plt.title("Crashes per month")
    plt.show()

def crashesOverTime():
    pass

if __name__ == "__main__":
    userChoice = int(input("What would you like to evaluate? (1, 2, 3)\n  1. crashes per month\n  2. reasons for crash\n  3. crashes per year\n$ "))

    if userChoice == 1:
        crashesPerMonth()
    elif userChoice == 2:
        reasonsForCrash()
    elif userChoice == 3:
        crashesOverTime()