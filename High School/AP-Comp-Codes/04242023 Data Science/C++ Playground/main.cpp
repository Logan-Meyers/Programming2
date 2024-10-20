#include <iostream>
#include <vector>
#include <random>
#include <chrono>
// custom classes
#include "QuickSort.h"

bool askIsGraphical() {
    std::string inputString;

    std::cout << "Should it be graphically displayed? (y/n)\n$ ";
    std::getline(std::cin, inputString);

    if (inputString == "y") {
        return true;
    }
    return false;
}

int askForArraySize() {
    int testAmount;

    std::cout << "How many (integer) tests do you want to test array sizes up to?\n$ ";
    std::cin >> testAmount;

    return testAmount;
}

std::vector<int> makeRandomList(int arraySize, int minVal = -100000, int maxVal = 100000) {
    // some random setup stuff
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(minVal, maxVal); // generate integers between min and max

    // the list to add values to
    std::vector<int> randomList;

    // generate and add values to list
    for (int i = 0; i < arraySize; ++i) {
        randomList.push_back(dist(gen));
    }

    // return list
    return randomList;
}

void printList(std::vector<int> listToPrint) {
    int listLength = listToPrint.size();
    
    std::cout << "[";
    for (int i = 0; i < listLength; i++) {
        std::cout << listToPrint[i];
        if (i < listLength-1) { std::cout << ", "; }
    }
    
    std::cout << "]\n";
}

void testWithPlot(int numOfTests) {
    std::cout << "haha no :D";
}

void testWithoutPlot(int numOfTests) {
    for (int i = 0; i < numOfTests; i++) {
        std::cout << "i is: " << i << "\n";
    }
    std::cout << "Done!";
}

// int main() {
//     // Get input from user
//     // graphical or not?
//     bool isGraphical = askIsGraphical();
//     // max array size to test to
//     int testAmount = askForArraySize();

//     // call quick sort functions
//     if (isGraphical) {
//         testWithPlot(testAmount);
//     } else {
//         testWithoutPlot(testAmount);
//     }

//     return 0;
// }

int main() {
    int arraySize;
    // get number of elements to sort
    std::cout << "Enter number of elements:\n$ ";
    std::cin >> arraySize;
    
    std::vector<int> randomList = makeRandomList(arraySize, -1000, 1000);

    QuickSort qs(randomList);

    // start measuring time
    auto start_time = std::chrono::high_resolution_clock::now();

    qs.sortArray();

    // stop measuring time
    auto end_time = std::chrono::high_resolution_clock::now();

    // calculate the time taken
    auto duration = end_time - start_time;
    double seconds = std::chrono::duration<double>(duration).count();

    printList(randomList);
    printList(qs.getSortedList());
    std::cout << "Iterations taken: " << qs.getIterations() << ".\n";
    std::cout << "Array size:       " << arraySize << "\n";
    std::cout << "Time taken:       " << seconds << " seconds\n";
}
