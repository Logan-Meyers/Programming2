#include <stdio.h>
#include <stdlib.h>

#define LIST_LEN 1000

void bubble_sort(int list[LIST_LEN]);

int main() {
    // init variables
    FILE *lists = fopen("two_lists.txt", "r");

    int left[LIST_LEN];
    int right[LIST_LEN];
    int total_distance = 0;
    int similarity_score = 0;

    // read numbers from file into lists
    for (int line = 0; line < LIST_LEN; line++) {
        fscanf(lists, "%d", left+line);
        fscanf(lists, "%d", right+line);
    }

    // sort lists
    bubble_sort(left);
    bubble_sort(right);

    // add distance between values to total
    for (int i=0; i < LIST_LEN; i++) {
        if (left[i] < right[i]) total_distance += right[i] - left[i];
        else if (right[i] < left[i]) total_distance += left[i] - right[i];
        else total_distance += 0;  // duh
    }

    // calculate similarity score
    // this would be done better with a frequency array,
    // but I'll do the worse way
    
    // loop through each value in the left list
    for (int i=0; i < LIST_LEN; i++) {
        // store val
        int curr_val = left[i];

        // find occurences in right list
        int occurences = 0;
        for (int ii=0; ii < LIST_LEN; ii++) {
            if (right[ii] == curr_val) occurences++;
        }

        printf("Found %d occurences of %d\n", occurences, curr_val);

        similarity_score += curr_val * occurences;
    }

    // print results
    printf("Total distance: %d\n", total_distance);
    printf("Similarity Score: %d\n", similarity_score);
}

void bubble_sort(int list[LIST_LEN]) {
    int u = LIST_LEN-1;  // end of list, [-1]
    while (u > 0) {      // while more than nothing unsorted
        int c = 1;       // second element
        while (c <= u) {
            if (list[c] < list[c-1]) {
                int tmp = list[c];
                list[c] = list[c-1];
                list[c-1] = tmp;
            }
            c++;  // haha
        }
        u--;
    }
}