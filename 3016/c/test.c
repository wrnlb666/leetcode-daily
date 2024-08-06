#include <stdio.h>
#include <stdlib.h>


int cmp_int(const void* arg1, const void* arg2) {
    return *(int*)arg2 - *(int*)arg1;
}


int minimumPushes(char* word) {
    // count frequency
    int count[26] = {0};
    for (char* c = word; *c != 0; c++) {
        count[*c - 0x61]++;
    }

    // sort by frequency
    qsort(count, 26, sizeof (int), cmp_int);

    // calculate
    int res = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] == 0) {
            break;
        }
        res += count[i] * ((i / 8) + 1);
    }

    return res;
}


int main(void) {
    char* word = "aabbccddeeffgghhiiiiii";
    int res = minimumPushes(word);
    printf("%d\n", res);

    return 0;
}
