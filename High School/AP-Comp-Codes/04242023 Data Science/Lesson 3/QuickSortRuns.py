import random
import QuickSort
import matplotlib.pyplot as plt


TESTS_TO_AVERAGE = 3

### functions for testing and evaluating etc etc
def getAverageOfList(lst: list):
    return sum(lst) / len(lst)

def runTestGetIterations(arraySize):
    array = None
    array = [random.randint(-10000000, 10000000) for _ in range(arraySize)]
    return QuickSort.quicksort(array)

def runTestsGetAverage(arraySize, numOfTests):
    iterationsToAverage = []

    for _ in range(numOfTests):
        iterations = runTestGetIterations(arraySize)
        iterationsToAverage.append(iterations)
    
    return getAverageOfList(iterationsToAverage)

### functions for running tests
def testWithDynamicPlot(numOfTests: int, numOfAverages: int):
    # set interactive mode on plt
    plt.ion()

    # function to plot graph stuff
    def plotGraph(pauseLength: float=0.1):
        plt.clf()
        plt.plot(arraySizeVals, iterationsVals, color="red")
        plt.ylabel(f"Average Num of Iterations")
        plt.xlabel("Size of Array")
        plt.title("QuickSort Efficiency!")
        plt.draw()
        plt.pause(pauseLength)

    # lists to hold data
    arraySizeVals = []
    iterationsVals = []

    # testing loop
    for testNum in range(numOfTests):
        # add to lists, calculate iterations for array size
        arraySizeVals.append(testNum+1)
        iterationsVals.append(runTestsGetAverage(testNum+1, numOfAverages))
        # update graph
        plotGraph(pauseLength=0.0001)
        # debugging
        print(f"Finished test with size of {testNum+1}")
    
    # show plot at end
    plt.ioff()
    plt.show()

def testWithStaticPlot(numOfTests: int, numOfAverages: int):
    # function to plot graph stuff
    def plotGraph():
        plt.plot(arraySizeVals, iterationsVals, color="red")
        plt.ylabel(f"Average Num of Iterations")
        plt.xlabel("Size of Array")
        plt.title("QuickSort Efficiency!")
        plt.show()
    
    # lists to hold data
    arraySizeVals = []
    iterationsVals = []

    # testing loop
    for testNum in range(numOfTests):
        # add to lists, calculate iterations for array size
        arraySizeVals.append(testNum+1)
        iterationsVals.append(runTestsGetAverage(testNum+1, numOfAverages))
        # debugging
        print(f"Finished test with size of {testNum+1}")
    
    # show plot at end
    plotGraph()

### main function
def main():
    dynamicPlot = input("Do you want the plot to draw as the tests are run through? (y/n)\n$ ")
    dynamicPlot = True if dynamicPlot.lower() == "y" else False

    testAmount = int(input("How many (integer) tests do you want to test array sizes up to?\n$ "))
    averageAmount = int(input("How many tests (integer) to average per array size?\n$ "))

    if dynamicPlot:
        testWithDynamicPlot(testAmount, averageAmount)
    else:
        testWithStaticPlot(testAmount, averageAmount)

### check if main
if __name__ == "__main__":
    main()
