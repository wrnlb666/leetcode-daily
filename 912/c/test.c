#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void merge(int* arr, int left, int mid, int right) {
    int l1 = mid - left + 1;
    int l2 = right - mid;

    int larr[l1];
    int rarr[l2];

    memcpy(larr, &arr[left], sizeof (int) * l1);
    memcpy(rarr, &arr[mid + 1], sizeof (int) * l2);

    int i = 0;
    int j = 0;
    int index = left;
    while (i < l1 && j < l2) {
        if (larr[i] <= rarr[j]) {
            arr[index] = larr[i];
            i += 1;
        } else if (larr[i] > rarr[j]) {
            arr[index] = rarr[j];
            j += 1;
        }
        index += 1;
    }

    if (i < l1) {
        memcpy(&arr[index], &larr[i], sizeof (int) * (l1 - i));
    }
    if (j < l2) {
        memcpy(&arr[index], &rarr[j], sizeof (int) * (l2 - j));
    }
}


void merge_sort(int* arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int mid = left + ((right - left) >> 1);
    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);

    merge(arr, left, mid, right);
}


int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* res = malloc(sizeof (int) * numsSize);
    memcpy(res, nums, sizeof (int) * numsSize);
    merge_sort(res, 0, numsSize - 1);
    return res;
}


int main(void) {
    int nums[] = {3,4,5,1,2,1,1,4,5,1,4};
    int numSize = sizeof (nums) / sizeof (int);
    int* returnSize = malloc(sizeof (int));

    int* res = sortArray(nums, numSize, returnSize);
    for (int i = 0; i < *returnSize; i++) {
        printf("%2d", res[i]);
    }
    printf("\n");

    return 0;
}
