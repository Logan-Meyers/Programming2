#include "linkedlist.c"

int main() {
    Node *pList = NULL;

    read_csv_and_insert(&pList, "songs.csv");

    printf("Before:\n");
    displayRecords(pList);

    sortRecords(&pList, 1, 10);

    printf("\nAfter:\n");
    displayRecords(pList);
 
    return 0;
}