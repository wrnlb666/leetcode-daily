#include <stdio.h>


int getLucky(char* s, int k) {
    int sum = 0;
    for (char* c = s; *c != 0; c++) {
        int num = *c - 96;
        if (num < 10) {
            sum += num;
        } else {
            sum += num / 10 + num % 10;
        }
    }
    for (int c = 1; c < k; c++) {
        int new_sum = 0;
        while (sum > 0) {
            new_sum += sum % 10;
            sum /= 10;
        }
        sum = new_sum;
    }
    return sum;
}


int main(void) {
    char* s = "leetcode";
    int k = 2;
    
    int res = getLucky(s, k);
    printf("%d\n", res);
    return 0;
}
