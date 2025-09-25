#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR_LEN 128

typedef struct {
    char title[MAX_STR_LEN];
    char artist[MAX_STR_LEN];
    char album[MAX_STR_LEN];
    int year;
    int duration_seconds; // duration in seconds
} Data;

typedef struct Node {
    Data data;
    struct Node* pPrev;
    struct Node* pNext;
} Node;

// Example function to create a new node
Node* create_node(const char* title, const char* artist, const char* album, int year, int duration_seconds) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (!node) return NULL;
    strncpy(node->data.title, title, MAX_STR_LEN);
    strncpy(node->data.artist, artist, MAX_STR_LEN);
    strncpy(node->data.album, album, MAX_STR_LEN);
    node->data.year = year;
    node->data.duration_seconds = duration_seconds;
    node->pPrev = NULL;
    node->pNext = NULL;
    return node;
}