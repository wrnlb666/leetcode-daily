#include <stdio.h>
#include <stdlib.h>

#define STBDS_NO_SHORT_NAMES
#define STB_DS_IMPLEMENTATION
#include <stb/stb_ds.h>

int subarraysDivByK(int* nums, int numsSize, int k) {
    typedef struct {
        int key;
        int value;
    } kv_t;
    int cs = 0;             // cumulative sum
    int count = 0;
    kv_t* map = NULL;
    int temp_key = 0;
    int temp_var = 1;
    stbds_hmput(map, temp_key, temp_var);

    for (int i = 0; i < numsSize; i++) {
        cs += nums[i];
        temp_key = cs % k;
        kv_t* ptr = stbds_hmgetp_null(map, temp_key);
        if (ptr != NULL) {
            count += ptr->value;
            ptr->value += 1;
            printf("%d, %d\n", cs, ptr->value);
        } else {
            temp_var = 1;
            stbds_hmput(map, temp_key, temp_var);
        }
    }
    stbds_hmfree(map);
    return count;
}

int main(void) {
    #define arrlength(arr) sizeof ((arr)) / sizeof (int)
    int nums[] = {4,5,0,-2,-3,1};
    int k = 5;
    printf("%d\n", subarraysDivByK(nums, arrlength(nums), k));
}
