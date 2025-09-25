#include "linkedlist.c"

int main() {
    Node *pList = NULL;

    read_csv_and_insert(&pList, "songs.csv");

    printf("Before:\n");
    print_list(pList);

    sortRecords(&pList, 1, 10);

    printf("\nAfter:\n");
    print_list(pList);
 
    return 0;
}