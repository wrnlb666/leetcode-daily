#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int minKBitFlips(int* nums, int nums_size, int k) {
    int res = 0;
    int flipped = 0;
    bool flip[nums_size];
    memset(flip, 0, sizeof (flip));

    for (int i = 0; i < nums_size; i++) {
        if (i >= k) {
            if (flip[i-k]) {
                flipped -= 1;
            }
        }
        if (flipped % 2 == nums[i]) {
            if (i + k > nums_size) {
                return -1;
            }
            flipped += 1;
            flip[i] = true;
            res += 1;
        }
    }

    return res;
}


int main(void) {
    int nums[] = {0,0,0,1,0,1,1,0};
    int nums_size = sizeof (nums) / sizeof (int);
    int k = 3;
    
    int res = minKBitFlips(nums, nums_size, k);
    printf("%d\n", res);

    return 0;
}
