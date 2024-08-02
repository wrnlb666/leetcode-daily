#include <stdio.h>


int minSwaps(int* nums, int numsSize) {
    int res = numsSize;
    int ones = 0;
    for (int i = 0; i < numsSize; i++) {
        ones += nums[i];
    }

    int count = nums[0];
    int end = 0;

    for (int start = 0; start < numsSize; start++) {
        if (start != 0) {
            count -= nums[start - 1];
        }

        while (end - start + 1 < ones) {
            end += 1;
            count += nums[end % numsSize];
        }

        res = res < (ones - count) ? res : (ones - count);
    }

    return res;
}


int main(void) {
    int nums[] = {0,1,0,1,1,0,0};
    int numsSize = sizeof (nums) / sizeof (int);

    int res = minSwaps(nums, numsSize);
    printf("%d\n", res);

    return 0;
}
