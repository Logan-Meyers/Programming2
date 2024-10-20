import random, time
import numpy as np


iterations = 0

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def partition(array, start, end):
    """ quicksort partitioning, using end """
    pivot = array[end]
    L = start
    R = end
    while L < R:
        while array[L] < pivot:
            L += 1
        while array[R] > pivot:
            R -= 1
        swap(array, L, R)
        # avoid hanging on the same numbers
        if ( array[L] == array[R] ):
            L += 1
    return R

def _quicksort(array, start, end):
    """ Recursive quicksort function """
    global iterations
    iterations += 1

    print("Recursive Sorting. Iterations:", iterations)

    if start < end:
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)

def quicksort(array):
    global iterations
    iterations = 0
    _quicksort(array, 0, len(array)-1)
    return iterations

if __name__ == "__main__":
    # array = [12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2]
    arraySize = int(input("Enter number of elements:\n$ "))
    array = [random.randint(-1000, 1000) for _ in range(arraySize)]
    npArray = np.array(array)
    print(npArray)

    input()

    start_time = time.time()

    quicksort(array)
    
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(array)
    print("Iterations taken:", iterations)
    print("Array size:      ", arraySize)
    print("Time taken:      ", elapsed_time)