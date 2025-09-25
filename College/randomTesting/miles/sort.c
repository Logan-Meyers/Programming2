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
                    print_list(*pList);
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
                        print_list(*pList);
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