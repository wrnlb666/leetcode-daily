#include <stdio.h>


int minBitFlips(int start, int goal) {
    int xor = start ^ goal;
    int res = 0;
    for (int i = 0; i < 31; i++) {
        if (xor & (1 << i)) {
            res += 1;
        }
    }
    return res;
}


int main(void) {
    int start = 10;
    int goal = 7;

    int res = minBitFlips(start, goal);
    printf("%d\n", res);
    return 0;
}
