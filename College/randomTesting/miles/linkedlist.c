#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.c" // Assumes node.c defines struct Node and basic node functions

// Insert at front
void insert_front(Node **head, const char* title, const char* artist, const char* album, int year, int duration_seconds) {
    Node *new_node = create_node(title, artist, album, year, duration_seconds);
    new_node->pNext = *head;
    new_node->pPrev = NULL;
    if (*head)
        (*head)->pPrev = new_node;
    *head = new_node;
}

// Insert at back (O(n) since no tail pointer)
void insert_back(Node **head, const char* title, const char* artist, const char* album, int year, int duration_seconds) {
    Node *new_node = create_node(title, artist, album, year, duration_seconds);
    new_node->pNext = NULL;
    new_node->pPrev = NULL;
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    Node *curr = *head;
    while (curr->pNext)
        curr = curr->pNext;
    curr->pNext = new_node;
    new_node->pPrev = curr;
}

// Delete a node (by pointer)
void delete_node(Node **head, Node *node) {
    if (!node) return;
    if (node->pPrev)
        node->pPrev->pNext = node->pNext;
    else
        *head = node->pNext;
    if (node->pNext)
        node->pNext->pPrev = node->pPrev;
    free(node);
}

// Print list forward
void displayRecords(Node *head) {
    Node *curr = head;
    while (curr != NULL) {
        printf("Title: %s, Artist: %s, Album: %s, Year: %d, Duration: %d\n",
               curr->data.title, curr->data.artist, curr->data.album, curr->data.year, curr->data.duration_seconds);
        curr = curr->pNext;
    }
}

// Free the entire list
void free_list(Node **head) {
    Node *curr = *head;
    while (curr) {
        Node *next = curr->pNext;
        free(curr);
        curr = next;
    }
    *head = NULL;
}

void read_csv_and_insert(Node **head, const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        perror("Failed to open CSV file");
        return;
    }

    char line[1024];
    fgets(line, sizeof(line), fp);  // skip header

    while (fgets(line, sizeof(line), fp)) {
        line[strcspn(line, "\r\n")] = 0;
        char *title = strtok(line, ",");
        char *artist = strtok(NULL, ",");
        char *album = strtok(NULL, ",");
        char *year_str = strtok(NULL, ",");
        char *duration_str = strtok(NULL, ",");

        if (!title || !artist || !album || !year_str || !duration_str)
            continue;

        int year = atoi(year_str);
        int duration = atoi(duration_str);

        insert_back(head, title, artist, album, year, duration);
    }

    fclose(fp);
}

void sortRecords(Node** pList, int choice, int listLength) {
    // VAR RENAME: pTemp2 -> pSorted; repurpose to point at the last node successfully sorted
    Node *pCur = *pList, *pTemp = pCur->pNext, *pSorted = NULL;

    switch (choice) {
        // by artist
        case 1:
            // CHANGED: `pCur->pNext != NULL`
            // loop while the last sorted node is not the node pointed to by list (head)
            while (*pList != pSorted) {
                // CHANGED: (from og), remvoed `->pNext`
                // loop while there is a next node to compare against
                while (pTemp != NULL) {

                    // debugging
                    printf("\nIn sort, before operations:\n");
                    displayRecords(*pList);
                    printf("artists: %s, %s, %d\n", pCur->data.artist, pTemp->data.artist, strcmp(pCur->data.artist, pTemp->data.artist));

                    // check if current's artist should be after next's artist
                    if (strcmp(pCur->data.artist, pTemp->data.artist) > 0) {

                        // switch current and next's nodes; shuffle pointers
                        pCur->pNext = pTemp->pNext;
                        if (pCur->pPrev) pCur->pPrev->pNext = pTemp;  // ADD: important, fix lost link to node who is now before current
                        if(pTemp->pNext) pTemp->pNext->pPrev = pCur;  // ADD: null check
                        pTemp->pNext = pCur;
                        pTemp->pPrev = pCur->pPrev;
                        pCur->pPrev = pTemp;

                        // pCur = pTemp;  // REMOVE: unnecessary

                        // fix swap at beginning case:
                        // set new list head to what was the 2nd element,
                        // by going back one node
                        if ((*pList)->pPrev != NULL) {
                            *pList = (*pList)->pPrev;
                        }

                        // debuggign
                        printf("\nIn sort, after operations:\n");
                        displayRecords(*pList);
                    }

                    // optimization step, also important for flow:
                    // break if the next is the closest sorted node
                    else if (pCur->pNext == pSorted) break;

                    // else, increment pCur to move onto the rest of the list to find other possibly larger values
                    else pCur = pCur->pNext;

                    // increment pTemp, the node after current
                    // pTemp = pTemp->pNext;  // REMOVE: handled in if

                    // pCur is now one more node along the list, with pTemp possibly behind or equal to pCur.
                    // set pTemp to pCur's next
                    if (pCur) pTemp = pCur->pNext;  // ADD: null check just in case
                }

                // set pSorted to current, which has now been placed as far back as it should be
                pSorted = pCur;

                // reset current to beginning
                pCur = *pList;
                if (pCur) pTemp = pCur->pNext;
            }

            break;
        default:
            break;
    }
}