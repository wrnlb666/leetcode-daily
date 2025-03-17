#include <stdbool.h>
#include <stdio.h>

bool divideArray(int* nums, int numsSize) {
    int cache[501] = {};
    for (int i = 0; i < numsSize; i++) {
        int n = nums[i];
        cache[n] = cache[n] ? 0 : 1;
    }
    for (int i = 0; i < 501; i++) {
        if (cache[i]) {
            return false;
        }
    }
    return true;
}

int main(void) {
    int  nums[] = {3, 2, 3, 2, 2, 2};
    int  numsSize = sizeof(nums) / sizeof(int);
    bool res = divideArray(nums, numsSize);
    printf("%s\n", res ? "True" : "False");
    return 0;
}
