#include <stdio.h>
#include <stdbool.h>


int itbs(int n) {
    int res = 0;
    for (int i = 0; i < 31; i++) {
        if (n & (1 << i)) {
            res += 1;
        }
    }
    return res;
}


bool canSortArray(int* nums, int numsSize) {
    int curr_bit = itbs(nums[0]);
    int curr_lar = nums[0];
    int last = 0;

    for (int i = 1; i < numsSize; i++) {
        int n = nums[i];
        int bs = itbs(n);
        if (bs == curr_bit) {
            if (n < last) {
                return false;
            }
            if (n > curr_lar) {
                curr_lar = n;
            }
        } else {
            last = curr_lar;
            if (n < last) {
                return false;
            }
            curr_bit = bs;
            curr_lar = n;
        }
    }

    return true;
}


int main(void) {
    int nums[] = {8,4,2,30,15};
    int numsSize = sizeof (nums) / sizeof (int);
    bool res = canSortArray(nums, numsSize);
    printf("%s\n", res ? "true" : "false");

    return 0;
}
