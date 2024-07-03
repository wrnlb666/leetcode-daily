#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <inttypes.h>


int minDifference(int* nums, int numsSize) {
    // early return
    if (numsSize <= 4) {
        return 0;
    }

    // record 4 smallest and 4 largest
    int64_t smallest[4] = { 10e9, 10e9, 10e9, 10e9 };
    int64_t largest[4] = { -10e9, -10e9, -10e9, -10e9 };
    
    // find 4 smallest and 4 largest
    for (int i = 0; i < numsSize; i++) {
        int n = nums[i];
        if (n > smallest[3] && n < largest[3]) {
            continue;
        }
        if (n <= smallest[3]) {
            if (n <= smallest[0]) {
                memmove(&smallest[1], &smallest[0], sizeof (int64_t) * 3);
                smallest[0] = n;
            } else if (n <= smallest[1]) {
                memmove(&smallest[2], &smallest[1], sizeof (int64_t) * 2);
                smallest[1] = n;
            } else if (n <= smallest[2]) {
                memmove(&smallest[3], &smallest[2], sizeof (int64_t) * 1);
                smallest[2] = n;
            } else {
                smallest[3] = n;
            }
        }
        if (n >= largest[3]) {
            if (n >= largest[0]) {
                memmove(&largest[1], &largest[0], sizeof (int64_t) * 3);
                largest[0] = n;
            } else if (n >= largest[1]) {
                memmove(&largest[2], &largest[1], sizeof (int64_t) * 2);
                largest[1] = n;
            } else if (n >= largest[2]) {
                memmove(&largest[3], &largest[2], sizeof (int64_t) * 1);
                largest[2] = n;
            } else {
                largest[3] = n;
            }
        }
    }

    // traverse smallest and largest to find min difference
    int res = largest[0] - smallest[3];
    for (int i = 0, j = 3; i < 4; i++, j--) {
        printf("%" PRId64 ", %" PRId64 "\n", largest[i], smallest[j]);
        int temp = largest[i] - smallest[j];
        if (temp < res) {
            res = temp;
        }
    }
    return res;
}


int main(void) {
    int nums[] = {6,6,0,1,1,4,6};
    int numsSize = sizeof (nums) / sizeof (int);

    int res = minDifference(nums, numsSize);
    printf("%d\n", res);
    
    return 0;
}
