// QuickSort.h
#ifndef QUICKSORT_H
#define QUICKSORT_H

class QuickSort {
    public:
        QuickSort(std::vector<int> arrayToSort);
        void sortArray();
        int getIterations();
        std::vector<int> getSortedList();
    private:
        bool isSorted;
        int iterations;
        void _quicksort(std::vector<int>& array, int start, int end);
        int partition(std::vector<int>& array, int start, int end);
        void swap(std::vector<int>& array, int i, int j);
        std::vector<int> sortingList;
};

#endif