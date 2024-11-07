#include <stdio.h>


int largestCombination(int* candidates, int candidatesSize) {
    int res = 0;
    for (int i = 0; i < 31; i++) {
        int curr = 0;
        for (int j = 0; j < candidatesSize; j++) {
            if (candidates[j] & (1 << i)) {
                curr += 1;
            }
        }
        if (curr > res) {
            res = curr;
        }
    }
    
    return res;
}


int main(void) {
    int candidates[] = {16,17,71,62,12,24,14};
    int candidatesSize = sizeof (candidates) / sizeof (int);
    int res = largestCombination(candidates, candidatesSize);
    printf("%d\n", res);

    return 0;
}
