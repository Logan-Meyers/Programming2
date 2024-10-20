#include <iostream>
#include <algorithm>
#include "QuickSort.h"


QuickSort::QuickSort(std::vector<int> listToSort) {
    // constructor
    sortingList = listToSort;
    isSorted = false;
}

void QuickSort::swap(std::vector<int>& array, int i, int j) {
    int tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
}

int QuickSort::partition(std::vector<int>& array, int start, int end) {
    // quicksort partitioning, using end

    // variable setup
    int pivot = array[end];
    int L = start + 0;
    int R = end + 0;

    // main while loop
    while (L < R) {
        // increment left
        while (array[L] < pivot) {
            L++;
        }
        // increment right
        while (array[R] > pivot) {
            R--;
        }
        // swap values
        swap(array, L, R);
        // avoid hanging on the same numbers
        if (array[L] == array[R]) {
            L++;
        }
    }
    // return right
    return R;
}

void QuickSort::_quicksort(std::vector<int>& array, int start, int end) {
    // recursive quicksort function
    //increment iteration count
    iterations++;

    std::cout << "Recursive sorting. Iterations: " << iterations << "\n"; 

    // run sorting if sorting hasn't reached the end
    if (start < end) {
        // get split
        int split = partition(array, start, end);
        _quicksort(array, start, split-1);
        _quicksort(array, split+1, end);
    }
}

void QuickSort::sortArray() {
    // equivalent to python's "quicksort" function for initial sorting
    iterations = 0;

    std::cout << "Sorting array\n";

    // call recursive sorting function
    _quicksort(sortingList, 0, sortingList.size()-1);
    // set sorted bool val
    isSorted = true;
}

int QuickSort::getIterations() {
    return iterations;
}

std::vector<int> QuickSort::getSortedList() {
    return sortingList;
}