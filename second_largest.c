#include <stdio.h>
int main() {
    int arr[100], n, first = -1, second = -1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    for (int i = 0; i < n; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second && arr[i] != first)
            second = arr[i];
    }
    printf("Second largest: %d\n", second);
    return 0;
}
