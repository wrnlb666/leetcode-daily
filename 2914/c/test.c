#include <stdio.h>


int minChanges(char* s) {
    int res = 0;
    char* first = s;
    char* second = s + 1;
    for (; *first != '\0'; first += 2, second += 2) {
        if (*first != *second) {
            res += 1;
        }
    }
    return res;
}


int main(void) {
    char* s = "1001";
    int res = minChanges(s);
    printf("%d\n", res);

    return 0;
}
