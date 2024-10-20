def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def bubblesort(array):
    n = len(array)-1
    for i in range(0, len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                swap(array, j+1, j)
        n -= 1
    return array

if __name__ == "__main__":
    array = [12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2]
    array = bubblesort(array)
    print(array)