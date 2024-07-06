#include <stdio.h>


int passThePillow(int n, int time) {
    int round = time / (n - 1);
    int mod = time % (n - 1);

    if (round % 2 == 0) {
        if (mod == 0) {
            return 1;
        } else {
            return mod + 1;
        }
    } else {
        if (mod == 0) {
            return n;
        } else {
            return n - mod;
        }
    }
}


int main(void) {
    int n = 3;
    int time = 2;
    int res = passThePillow(n, time);
    printf("%d\n", res);

    return 0;
}
