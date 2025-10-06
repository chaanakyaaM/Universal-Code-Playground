# Title: Linked List
# Topic: DataStructures
# Language: c

#include <stdio.h>
#include <stdlib.h>

struct Node { int data; struct Node *next; };

int main() {
    struct Node *head = malloc(sizeof(struct Node));
    head->data = 10; head->next = malloc(sizeof(struct Node));
    head->next->data = 20; head->next->next = NULL;

    for(struct Node *p = head; p != NULL; p = p->next)
        printf("%d -> ", p->data);
    printf("NULL\n");
}
