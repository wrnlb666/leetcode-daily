#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


static inline int modulo(int a, int b) {
    return ((a % b) + b) % b;
}


bool canArrange(int* arr, int arrSize, int k) {
    int* mod = calloc(k, sizeof (int));
    for (int i = 0; i < arrSize; i++) {
        mod[modulo(arr[i], k)] += 1;
    }

    bool res = false;
    if (mod[0] % 2 != 0) {
        goto cleanup;
    }
    for (int i = 1, j = k-1; i < j; i++, j--) {
        if (mod[i] != mod[j]) {
            goto cleanup;
        }
    }
    res = true;

cleanup:
    free(mod);
    return res;
}


int main(void) {
    int arr[] = {-1,-1,-1,-1,2,2,-2,-2};
    int k = 3;
    bool res = canArrange(arr, sizeof (arr) / sizeof (int), k);
    printf("%s\n", res ? "True" : "False");

    return 0;
}
