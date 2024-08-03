#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int cmp_int(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}


bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    qsort(target, targetSize, sizeof (int), cmp_int);
    qsort(arr, arrSize, sizeof (int), cmp_int);

    for (int i = 0; i < targetSize; i++) {
        if (target[i] != arr[i]) {
            return false;
        }
    }
    return true;
}


int main(void) {
    int target[] = {1,2,3,4};
    int targetSize = sizeof (target) / sizeof (int);
    int arr[] = {2,4,1,3};
    int arrSize = sizeof (arr) / sizeof (int);

    bool res = canBeEqual(target, targetSize, arr, arrSize);
    printf("%s\n", res ? "true" : "false");
    return 0;
}
