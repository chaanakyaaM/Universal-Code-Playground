// Title: Linear Search
// Topic: Algorithms
// Language: c

#include <stdio.h>
int main() {
    int arr[] = {10, 20, 30, 40}, n = 4, key;
    printf("Enter key: ");
    scanf("%d", &key);
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return printf("Found at %d", i), 0;
    printf("Not found");
}
