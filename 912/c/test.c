#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define swap(a, b) \
do { \
    int t = a; \
    a = b; \
    b = t; \
} while (0)


int partition(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}


void quick_sort(int* nums, int low, int high) {
    if (low >= high) {
        return;
    }
    
    int pivot = partition(nums, low, high);
    quick_sort(nums, low, pivot - 1);
    quick_sort(nums, pivot + 1, high);
}


int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* res = malloc(sizeof (int) * numsSize);
    memcpy(res, nums, sizeof (int) * numsSize);
    quick_sort(res, 0, numsSize - 1);
    return res;
}


int main(void) {
    int nums[] = {5,2,3,1};
    int numSize = sizeof (nums) / sizeof (int);
    int* returnSize = malloc(sizeof (int));

    int* res = sortArray(nums, numSize, returnSize);
    for (int i = 0; i < *returnSize; i++) {
        printf("%2d", res[i]);
    }
    printf("\n");

    return 0;
}
